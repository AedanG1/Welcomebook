from django.shortcuts import render, redirect
from .models import Rule, Information, Eats
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import RuleForm, InfoImageForm, EatsImageForm

import json


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def house_rules_admin(request):
    rules = Rule.objects.all()
    context = {
        "rules": rules,
        "form": RuleForm
    }
    return render(request, "app/house_rules_admin.html", context)


def eats_admin(request):
    eats = Eats.objects.all()
    form = EatsImageForm
    context = {
       "form": form,
       "eats": eats 
    }
    return render(request, "app/eats_admin.html", context)


def information_admin(request):
    infos = Information.objects.all()
    form = InfoImageForm
    context = {
        "infos": infos,
        "form": form
    }
    return render(request, "app/information_admin.html", context)


@csrf_exempt
def add_new_item(request):
    if request.method == "POST":
        data = json.loads(request.body)
        type = data.get("type")
        if type == "rule":
            rules_total = Rule.objects.all().count()
            new_rule = Rule(
                text = "New rule",
                subtext = "rule",
                position = rules_total + 1
            )
            new_rule.save()
        elif type == "info":
            info_total = Information.objects.all().count()
            new_info = Information(
                title = "New info",
                text = "information",
                subtext = "subtext",
                position = info_total + 1
            )
            new_info.save()
        elif type == "eats":
            eats_total = Eats.objects.all().count()
            new_eats = Eats(
                title = "New restaurant",
                drive_time = 1,
                text = "description",
                website = "example.com",
                phone = 1234567890,
                position = eats_total + 1 
            )
            new_eats.save()
        return JsonResponse({
            "success": "New item created"
        }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)


@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        type = data.get("type")
        if type == 'rule':
            item = Rule.objects.get(pk=item_id)
        elif type == 'info':
            item = Information.objects.get(pk=item_id)
        elif type == 'eats':
            item = Eats.objects.get(pk=item_id)
        item.delete()
        return JsonResponse({
            "success": "item deleted"
        }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)


@csrf_exempt
def edit_position(request):
    if request.method == "POST":
        data = json.loads(request.body)
        type = data.get("type")
        if type == "rule":
            item_model = Rule
        elif type == "info":
            item_model = Information 
        elif type == "eats":
            item_model = Eats
            
        for index, item_id in enumerate(data["positions"]):
            item = item_model.objects.get(pk=item_id)
            item.position = index
            item.save()
        return JsonResponse({
            "success": "Eats order saved"
        }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)


def upload_image(request, info_id):
    info = Information.objects.get(pk=info_id)
    if request.method == 'POST':
        form = InfoImageForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            return redirect('information_admin')
    else:
        return redirect('information_admin')


@csrf_exempt
def edit_rule(request, rule_id):
    rule = Rule.objects.get(pk=rule_id)

    if request.method == "POST":
        data = json.loads(request.body)
        if data.get("text") is not None:
            rule.text = data["text"]
            rule.subtext = data.get("subtext", "")
            rule.save()
            return JsonResponse({
                "success": "Changes saved"
            }, status=200)
            
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)

@csrf_exempt
def edit_info(request, info_id):
    info = Information.objects.get(pk=info_id)
    if request.method == "POST":
        data = json.loads(request.body)
        if data.get("text") is not None:
            info.title = data["title"]
            info.text = data["text"]
            info.subtext = data.get("subtext", "")
            info.save()
            return JsonResponse({
                "success": "Changes saved"
            }, status=200)
        if data.get("remove_img") is not None:
            info.image = None
            info.save()
            return JsonResponse({
                "success": "Image removed"
            }, status=200)
    else:
        return JsonResponse({
            "error": "PUT request required"
        }, status=400)
    

@csrf_exempt
def edit_eats(request, eats_id):
    eats = Eats.objects.get(pk=eats_id)
    if request.method == "POST":
        data = json.loads(request.body)
        if data.get("text") is not None:
            eats.title = data["title"]
            eats.drive_time = data["drive"]
            eats.text = data["text"]
            eats.website = data["website"]
            eats.phone = data["phone"]
            eats.save()
            return JsonResponse({
                "success": "Changes saved"
            }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)

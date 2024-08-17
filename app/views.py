from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Rule, Information, Eats, Activity

from .forms import RuleForm, InfoImageForm, EatsImageForm, ActivityImageForm

import json

MODELS = {
    "rule": Rule,
    "info": Information,
    "eats": Eats,
    "activity": Activity
}

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


def activity_admin(request):
    activitys = Activity.objects.all()
    form = ActivityImageForm
    context = {
        "activitys": activitys,
        "form": form
    }
    return render(request, "app/activity_admin.html", context)


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
def edit_item(request, item_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        type = data.get("type") 
        item_model = MODELS.get(type)
        item = item_model.objects.get(pk=item_id)

        skip = True
        for key in data:
            if skip:
                skip = False
                continue
            setattr(item, key, data[key])
        item.save()

        return JsonResponse({
            "success": "Changes saved"
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
        item_model = MODELS.get(type)
        item = item_model.objects.get(pk=item_id)
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
        item_model = MODELS.get(type)
            
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


def upload_image(request, item_id):
    if request.method == 'POST':
        type = request.POST.get('type')
        if type == 'info':
            path = 'information_admin'
            info = Information.objects.get(pk=item_id)
            form = InfoImageForm(request.POST, request.FILES, instance=info)
        elif type == 'eats':
            path = 'eats_admin'
            eats = Eats.objects.get(pk=item_id)
            form = EatsImageForm(request.POST, request.FILES, instance=eats)
        elif type == 'activity':
            path = 'activity_admin'
            activity = Activity.objects.get(pk=item_id)
            form = ActivityImageForm(request.POST, request.FILES, instance=activity)

        if form.is_valid():
            form.save()
            return redirect(path)
    else:
        return redirect(path)

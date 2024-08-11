from django.shortcuts import render, redirect
from .models import Rule, Information
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import RuleForm

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


@csrf_exempt
def add_new_rule(request):
    rules_total = Rule.objects.all().count()
    if request.method == "POST":
        data = json.loads(request.body)
        if data.get("text") is not None:
            new_rule = Rule(
                text = data["text"],
                position = rules_total + 1
            )
            new_rule.save()
            return JsonResponse({
                "success": "Added new rule"
            }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)


@csrf_exempt
def delete_rule(request, rule_id):
    rule = Rule.objects.get(pk=rule_id)    

    if request.method == "POST":
        data = json.loads(request.body)
        if data.get("rule_id") is not None:
            rule.delete()
            return JsonResponse({
                "success": "Deleted"
            }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)        


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
def edit_position(request):
    if request.method == "POST":
        data = json.loads(request.body)
        for index, rule_id in enumerate(data["positions"]):
            rule = Rule.objects.get(pk=rule_id)
            rule.position = index
            rule.save()
        return JsonResponse({
            "success": "Order saved"
        }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)

 
def information_admin(request):
    infos = Information.objects.all()
    context = {
        "infos": infos
    }
    return render(request, "app/information_admin.html", context)


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
    else:
        return JsonResponse({
            "error": "PUT request required"
        }, status=400)
    

@csrf_exempt
def add_new_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get("title") is not None:
            new_info = Information(
                title = data["title"],
                text = data["text"],
                subtext = data["subtext"]
            )
            new_info.save()
            return JsonResponse({
                "success": "New info added"
            })
        
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)

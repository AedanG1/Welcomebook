from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Rule, Information, Eats, Activity, Contacts, About

from .forms import InfoImageForm, EatsImageForm, ActivityImageForm

import json

MODELS = {
    "rule": Rule,
    "info": Information,
    "eats": Eats,
    "activity": Activity,
    "contacts": Contacts
}

# USER PAGES
def admin_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password"
            })
    else:
        return render(request, 'app/login.html')


def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def index(request):
    return render(request, "app/index.html")


def about_page(request):
    about = get_object_or_404(About)
    context = {
        "about": about
    }
    return render(request, 'app/about_page.html', context)


def activity_page(request):
    activitys = Activity.objects.all()
    context = {
        "activitys": activitys
    }
    return render(request, 'app/activity_page.html', context)


def house_rules_page(request):
    rules = Rule.objects.all()
    context = {
        "rules": rules
    }
    return render(request, 'app/house_rules_page.html', context)


def contacts_page(request):
    contacts = Contacts.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'app/contacts_page.html', context)


def information_page(request):
    infos = Information.objects.all()
    context = {
        "infos": infos
    }
    return render(request, 'app/information_page.html', context)


def eats_page(request):
    eats = Eats.objects.all()
    context = {
        "eats": eats
    }
    return render(request, 'app/eats_page.html', context)


# ADMIN PAGES
@login_required
def house_rules_admin(request):
    rules = Rule.objects.all()
    context = {
        "rules": rules,
    }
    return render(request, "app/house_rules_admin.html", context)


@login_required
def eats_admin(request):
    eats = Eats.objects.all()
    form = EatsImageForm
    context = {
       "form": form,
       "eats": eats 
    }
    return render(request, "app/eats_admin.html", context)


@login_required
def information_admin(request):
    infos = Information.objects.all()
    form = InfoImageForm
    context = {
        "infos": infos,
        "form": form
    }
    return render(request, "app/information_admin.html", context)


@login_required
def activity_admin(request):
    activitys = Activity.objects.all()
    form = ActivityImageForm
    context = {
        "activitys": activitys,
        "form": form
    }
    return render(request, "app/activity_admin.html", context)


@login_required
def about_admin(request):
    about = get_object_or_404(About)
    context = {
        "about": about
    }
    return render(request, "app/about_admin.html", context)


@login_required
def contacts_admin(request):
    contacts = Contacts.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, "app/contacts_admin.html", context)


# ADMIN FUNCTIONS
@login_required
def save_about(request):
    if request.method == "POST":
        about = get_object_or_404(About)
        data = json.loads(request.body)
        about.html_content = data["html"]
        about.save()
        return JsonResponse({
            "success": "Changes saved"
        }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)


@login_required
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
        elif type == "activity":
            activity_total = Activity.objects.all().count()
            new_activity = Activity(
                title = "New activity",
                drive_time = 1,
                text = "description",
                website = "example.com",
                position = activity_total + 1
            )
            new_activity.save()
        elif type == "contacts":
            contacts_total = Contacts.objects.all().count()
            new_contacts = Contacts(
                title = "New contact",
                phone = 1234567890,
                address_one = "123 Example St",
                address_two = "Exampleton EX 98765",
                position = contacts_total + 1
            )
            new_contacts.save()

        return JsonResponse({
            "success": "New item created"
        }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
def remove_image(request, item_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        type = data.get("type")
        item_model = MODELS.get(type)
        item = item_model.objects.get(pk=item_id)
        item.image = None
        item.save()
        return JsonResponse({
            "success": "Image removed"
        }, status=200)
    else:
        return JsonResponse({
            "error": "POST request required"
        }, status=400)

from django.forms import ModelForm, Textarea, HiddenInput
from .models import Rule, Information, Eats, Activity

class InfoImageForm(ModelForm):
    class Meta:
        model = Information
        fields = ["image"]
        labels = {
            "image": ""
        }


class EatsImageForm(ModelForm):
    class Meta:
        model = Eats
        fields = ["image"]
        labels = {
            "image": ""
        }


class ActivityImageForm(ModelForm):
    class Meta:
        model = Activity
        fields = ["image"]
        labels = {
            "image": ""
        }
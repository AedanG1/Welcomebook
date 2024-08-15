from django.forms import ModelForm, Textarea, HiddenInput
from .models import Rule, Information

class RuleForm(ModelForm):
    class Meta:
        model = Rule
        fields = ["text", "subtext"] 
        widgets = {
            "text": Textarea(attrs={'rows': "2", 'cols': "15"}),
            "subtext": Textarea(attrs={'rows': "2", 'cols': "15"})
        }
        lables = {
            "text": "Text",
            "subtext": "Subtext"
        }

class ImageUploadForm(ModelForm):
    class Meta:
        model = Information
        fields = ["image"]
        
        labels = {
            "image": ""
        }
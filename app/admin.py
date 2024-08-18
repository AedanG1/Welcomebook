from django.contrib import admin
from app.models import Rule, Information, Eats, Activity, About

# Register your models here.
admin.site.register(Rule)
admin.site.register(Information)
admin.site.register(Eats)
admin.site.register(Activity)
admin.site.register(About)
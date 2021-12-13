from django.contrib import admin

# Register your models here.
from .models import Character, Line

admin.site.register(Character)
admin.site.register(Line)

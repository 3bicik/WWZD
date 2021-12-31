from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Character, Line

# Register your models here.

admin.site.register(Character)
admin.site.register(Line)
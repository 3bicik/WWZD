from django.contrib import admin
from django.contrib.admin.decorators import register

# from .models import Character, Line
from .models import Character

# Register your models here.

admin.site.register(Character)
# admin.site.register(Line)
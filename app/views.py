from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from .models import Character
from .serializers import CharacterSerializer
from .text_to_sentiment import predict, sample_predict, pred

from django.core import serializers

# Create your views here.
def home(request):
    return HttpResponse('HOME')

def whole_predict(request):
    Character.objects.all().delete()
    predict()
    return get_json(request)

def test_predict(request):
    Character.objects.all().delete()
    sample_predict()
    return get_json(request)

def s01e01(request):
    Character.objects.all().delete()
    pred("s01e01")
    return get_json(request)

def s01e02(request):
    Character.objects.all().delete()
    pred("s01e02")
    return get_json(request)

def s01e03(request):
    Character.objects.all().delete()
    pred("s01e03")
    return get_json(request)

def s01e04(request):
    Character.objects.all().delete()
    pred("s01e04")
    return get_json(request)

def s01e05(request):
    Character.objects.all().delete()
    pred("s01e05")
    return get_json(request)

def s01e06(request):
    Character.objects.all().delete()
    pred("s01e06")
    return get_json(request)

def s01e07(request):
    Character.objects.all().delete()
    pred("s01e07")
    return get_json(request)

def s01e08(request):
    Character.objects.all().delete()
    pred("s01e08")
    return get_json(request)

def s01e09(request):
    Character.objects.all().delete()
    pred("s01e09")
    return get_json(request)

def s01e10(request):
    Character.objects.all().delete()
    pred("s01e10")
    return get_json(request)

def s01e11(request):
    Character.objects.all().delete()
    pred("s01e11")
    return get_json(request)

def s01e12(request):
    Character.objects.all().delete()
    pred("s01e12")
    return get_json(request)

def s01e13(request):
    Character.objects.all().delete()
    pred("s01e13")
    return get_json(request)

def get_json(request):
    objects = Character.objects.all()
    data = serializers.serialize('json', objects)
    return HttpResponse(data, content_type='application/json')

class ListCharacters(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class DetailCharacter(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

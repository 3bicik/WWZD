from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from .models import Character
from .serializers import CharacterSerializer
from .text_to_sentiment import predict, sample_predict

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

from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from .models import Character, Line
from .serializers import CharacterSerializer, LineSerializer


class ListCharacter(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class DetailCharacter(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
class ListLine(generics.ListCreateAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class DetailLine(generics.RetrieveUpdateDestroyAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer

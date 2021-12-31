from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from .models import Character, Line
from .serializers import CharacterSerializer, LineSerializer
from .data_loader import load_csv_to_database
from .text_to_sentiment import predict

# Create your views here.
def home(request):
    return HttpResponse('HOME')

def load_data(request):
    load_csv_to_database()
    return HttpResponse('Loading records from csv to database')

def test_predict(request):
    predict()
    return HttpResponse('Predicting sample data')

class ListCharacters(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class DetailCharacter(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
class ListLines(generics.ListCreateAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class DetailLine(generics.RetrieveUpdateDestroyAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
# todos/serializers.py
from rest_framework import serializers
from .models import Character, Line


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'personality',
        )
        model = Character

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'text',
            'emotion',
        )
        model = Line   


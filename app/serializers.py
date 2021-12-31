from rest_framework import serializers
from .models import Character, Line


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'personality',
        )
        model = Character

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'text',
            'emotion',
        )
        model = Line   
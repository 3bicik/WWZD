from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'sentiment',
            'number_of_lines'
        )
        model = Character

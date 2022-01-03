from rest_framework import serializers
# from .models import Character, Line
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'sentiment',
            'number_of_lines'
        )
        model = Character

# class LineSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'name',
#             'text',
#             'sentiment',
#         )
#         model = Line   
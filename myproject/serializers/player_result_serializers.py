
from rest_framework import serializers 
from player_result.models import PlayerResult


class PlayerResultListSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlayerResult
        fields='__all__'

class PlayerResultRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlayerResult
        fields=['red_cards','yellow_cards']

class PlayerResultWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlayerResult
        fields='__all__'

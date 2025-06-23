
from rest_framework import serializers 
from  player.models import Player

class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Player
        fields='__all__'

class PlayerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model= Player
        fields=['player_id','team']

class PlayerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Player
        fields='__all__'

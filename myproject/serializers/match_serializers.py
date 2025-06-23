from rest_framework import serializers 
from  match.models import Match

class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Match

        fields='__all__'

class MatchRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model= Match
        fields=['match_id','date']

class MatchWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Match
        fields='__all__'
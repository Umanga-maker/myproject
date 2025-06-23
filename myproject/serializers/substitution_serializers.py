
from rest_framework import serializers 

from substitution.models import Substitution

class SubstitutionListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Substitution
        fields='__all__'

class SubstitutionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model= Substitution
        fields=['player_in','player_out']

class SubstitutionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Substitution
        fields='__all__'

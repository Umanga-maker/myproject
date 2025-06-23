
from rest_framework import serializers 
from  team.models import Team

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Team
        fields='__all__'

class TeamRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model= Team
        fields=['id','name']

class TeamWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Team
        fields='__all__'

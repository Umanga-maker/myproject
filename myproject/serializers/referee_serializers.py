
from rest_framework import serializers 
from  referee.models import Referee
class RefereeListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Referee
        fields='__all__'

class RefereeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model= Referee
        fields=['years_of_experience','date_of_birth']

class RefereeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Referee
        fields='__all__'

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from player_result.models import PlayerResult
from serializers.player_result_serializers import (
    PlayerResultListSerializer,
    PlayerResultRetrieveSerializer,
    PlayerResultWriteSerializer,
)

class PlayerResultViewSet(viewsets.ModelViewSet):
    queryset = PlayerResult.objects.all()
    serializer_class = PlayerResultListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['player_result_id', 'player__name', 'match__id']
    ordering_fields = ['goals', 'assists', 'minutes_played']
    filterset_fields = {
        'player_result_id': ['exact'],
        'player': ['exact'],
        'match': ['exact'],
        'goals': ['gte', 'lte'],
        'assists': ['gte', 'lte'],
        'minutes_played': ['gte', 'lte'],
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PlayerResultWriteSerializer
        elif self.action == 'retrieve':
            return PlayerResultRetrieveSerializer
        return PlayerResultListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from player.models import Player
from serializers.player_serializers import (
    PlayerListSerializer,
    PlayerRetrieveSerializer,
    PlayerWriteSerializer,
)
from rest_framework.permissions import IsAuthenticated  # or your custom one
from rest_framework_simplejwt.authentication import JWTAuthentication
# from player.utilities.pagination import MyPageNumberPagination # or your actual module

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    # permission_classes = [playerPermission]
    authentication_classes = [JWTAuthentication]
    # pagination_class = MyPageNumberPagination
    serializer_class = PlayerListSerializer  # Default fallback

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']
    filterset_fields = {
        'id': ['exact'],
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PlayerWriteSerializer
        elif self.action == 'retrieve':
            return PlayerRetrieveSerializer
        return PlayerListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
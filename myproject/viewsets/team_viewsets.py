from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from team.models import Team
from serializers.team_serializers import (  
    TeamListSerializer,
    TeamRetrieveSerializer,
    TeamWriteSerializer,
)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  # Optional
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'name']
    filterset_fields = {'id': ['exact'], 'name': ['icontains']}

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TeamWriteSerializer
        elif self.action == 'retrieve':
            return TeamRetrieveSerializer
        return TeamListSerializer
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
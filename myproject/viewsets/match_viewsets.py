from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from match.models import Match
from serializers.match_serializers import (
    MatchListSerializer,
    MatchRetrieveSerializer,
    MatchWriteSerializer,
)

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['match_id', 'location', 'home_team__name', 'away_team__name']
    ordering_fields = ['match_date', 'location']
    filterset_fields = {
        'match_id': ['exact'],
        'match_date': ['exact', 'gte', 'lte'],
        'home_team': ['exact'],
        'away_team': ['exact'],
        'location': ['icontains'],
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MatchWriteSerializer
        elif self.action == 'retrieve':
            return MatchRetrieveSerializer
        return MatchListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
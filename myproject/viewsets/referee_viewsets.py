
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from referee.models import Referee
from serializers.referee_serializers import (
    RefereeListSerializer,
    RefereeRetrieveSerializer,
    RefereeWriteSerializer,
)

class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['referee_id', 'name', 'country']
    ordering_fields = ['referee_id', 'name', 'experience_years']
    filterset_fields = {
        'referee_id': ['exact'],
        'name': ['icontains'],
        'country': ['icontains']
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return RefereeWriteSerializer
        elif self.action == 'retrieve':
            return RefereeRetrieveSerializer
        return RefereeListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from substitution.models import Substitution
from serializers.substitution_serializers import (
    SubstitutionListSerializer,
    SubstitutionRetrieveSerializer,
    SubstitutionWriteSerializer,
)

class SubstitutionViewSet(viewsets.ModelViewSet):
    queryset = Substitution.objects.all()
    serializer_class = SubstitutionListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['substitution_id', 'match', 'player_in', 'player_out']
    ordering_fields = ['substitution_id', 'substitution_time']
    filterset_fields = {
        'substitution_id': ['exact'],
        'match': ['exact'],
        'player_in': ['exact'],
        'player_out': ['exact'],
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SubstitutionWriteSerializer
        elif self.action == 'retrieve':
            return SubstitutionRetrieveSerializer
        return SubstitutionListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

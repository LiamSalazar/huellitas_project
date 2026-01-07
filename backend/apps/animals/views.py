from rest_framework import viewsets, permissions 
from huellitas_config.permissions import IsStaffOrReadOnly
from rest_framework import viewsets
from huellitas_config.permissions import IsStaffOrReadOnly
from .models import Animal, ExpedienteAnimalCompleto
from .serializers import AnimalSerializer, ExpedienteAnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsStaffOrReadOnly] # Todos ven, Staff edita

class ExpedienteAnimalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExpedienteAnimalCompleto.objects.all()
    serializer_class = ExpedienteAnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Público puede ver el expediente
from rest_framework import viewsets, permissions 
from .models import Persona, Voluntario, DashboardVoluntarios
from .serializers import PersonaSerializer, VoluntarioSerializer, DashboardVoluntariosSerializer
from huellitas_config.permissions import IsDirector

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAdminUser] # Solo personal autorizado

class VoluntarioViewSet(viewsets.ModelViewSet):
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer
    permission_classes = [permissions.IsAdminUser]

class DashboardVoluntariosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DashboardVoluntarios.objects.all()
    serializer_class = DashboardVoluntariosSerializer
    permission_classes = [IsDirector]
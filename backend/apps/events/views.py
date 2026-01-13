from rest_framework import viewsets, permissions
from huellitas_config.permissions import IsStaffOrReadOnly
from .models import Evento, Eventoasistente
from .serializers import EventoSerializer, EventoAsistenteSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsStaffOrReadOnly]

class EventoAsistenteViewSet(viewsets.ModelViewSet):
    queryset = Eventoasistente.objects.all()
    serializer_class = EventoAsistenteSerializer
from rest_framework import serializers
from .models import Evento, Eventoasistente

class EventoSerializer(serializers.ModelSerializer):
    # Campo para ver la sede donde será el evento
    sede_nombre = serializers.ReadOnlyField(source='id_sede.nombre_sede')

    class Meta:
        model = Evento
        fields = '__all__'

class EventoAsistenteSerializer(serializers.ModelSerializer):
    nombre_asistente = serializers.ReadOnlyField(source='id_persona.nombre_persona')
    
    class Meta:
        model = Eventoasistente
        fields = '__all__'
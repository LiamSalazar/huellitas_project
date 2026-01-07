from rest_framework import serializers
from .models import Persona, Voluntario, Voluntariorol, Direccion, DashboardVoluntarios

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    # Mostramos la dirección completa si existe
    direccion_detalle = DireccionSerializer(source='id_direccion', read_only=True)

    class Meta:
        model = Persona
        # Excluimos pass_persona por seguridad
        fields = [
            'id_persona', 'nombre_persona', 'apellidos_persona', 
            'telefono_persona', 'email_persona', 'direccion_detalle'
        ]

class VoluntarioSerializer(serializers.ModelSerializer):
    # Anidamos los datos de la persona para que el Front vea quién es el voluntario
    datos_personales = PersonaSerializer(source='id_persona', read_only=True)
    rol_nombre = serializers.ReadOnlyField(source='id_voluntariorol.nombre_voluntariorol')

    class Meta:
        model = Voluntario
        fields = ['id_voluntario', 'datos_personales', 'rol_nombre', 'cedula_profesional_voluntario']

class DashboardVoluntariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardVoluntarios
        fields = '__all__'
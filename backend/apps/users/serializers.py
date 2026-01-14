from rest_framework import serializers
from .models import Persona, Voluntario, Voluntariorol, Direccion, DashboardVoluntarios
from django.contrib.auth.hashers import make_password
from apps.animals.models import Sede


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    direccion_detalle = DireccionSerializer(source='id_direccion', read_only=True)

    class Meta:
        model = Persona
        # ¡IMPORTANTE! Agregamos 'pass_persona' aquí
        fields = [
            'id_persona', 'nombre_persona', 'apellidos_persona', 
            'telefono_persona', 'email_persona', 'pass_persona', 'direccion_detalle'
        ]
        # Esto hace que la contraseña se reciba pero no se muestre en el JSON de respuesta
        extra_kwargs = {
            'pass_persona': {'write_only': True}
        }

    # El método create debe ir FUERA de la clase Meta
    def create(self, validated_data):
        # Extraemos la contraseña, la encriptamos y la guardamos
        password = validated_data.pop('pass_persona', None)
        instance = super().create(validated_data)
        if password:
            instance.pass_persona = make_password(password)
            instance.save()
        return instance

class VoluntarioSerializer(serializers.ModelSerializer):
    id_persona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())
    datos_personales = PersonaSerializer(source='id_persona', read_only=True)
    
    class Meta:
        model = Voluntario
        # Asegúrate de incluir id_persona para que el POST funcione
        fields = '__all__'

class DashboardVoluntariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardVoluntarios
        fields = '__all__'

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class VoluntariorolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntariorol
        fields = '__all__'
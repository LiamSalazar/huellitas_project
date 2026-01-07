from rest_framework import serializers
from .models import Procesoadopcion, Procesoadopcionestado, ValidarAdoptante
from apps.animals.models import Animal

class ProcesoAdopcionSerializer(serializers.ModelSerializer):
    # Usamos getattr por seguridad con los nombres de los campos
    nombre_animal = serializers.SerializerMethodField()
    estado_nombre = serializers.ReadOnlyField(source='id_procesoadopcionestado.nombre_procesoadopcionestado')

    class Meta:
        model = Procesoadopcion
        fields = '__all__'

    def get_nombre_animal(self, obj):
        return obj.id_animal.nombre_animal if obj.id_animal else "Sin nombre"

    # LA REGLA 
    def validate(self, data):
        animal = data.get('id_animal')
        # Buscamos si ya existe un proceso 'Iniciado' para este animal
        proceso_activo = Procesoadopcion.objects.filter(
            id_animal=animal, 
            id_procesoadopcionestado__nombre_procesoadopcionestado='Iniciado'
        ).exists()

        if proceso_activo:
            raise serializers.ValidationError(
                f"El animal {animal.nombre_animal} ya tiene un proceso de adopción en curso."
            )
        return data
    
class ValidarAdoptanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidarAdoptante
        fields = '__all__'
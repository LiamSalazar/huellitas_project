from rest_framework import serializers
from .models import (
    Animal, Animalespecie, Animalsexo, Animaltalla, 
    Animalestado, Razaperro, Razagato, Sede, ExpedienteAnimalCompleto
)

# --- Serializers de Catálogo (Para selects en el Frontend) ---

class AnimalEspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animalespecie
        fields = '__all__'

class AnimalSexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animalsexo
        fields = '__all__'

# --- Serializer Principal del Animal ---

class AnimalSerializer(serializers.ModelSerializer):
    # Campos calculados para mostrar texto en lugar de IDs
    especie_nombre = serializers.ReadOnlyField(source='id_animalespecie.nombre_animalespecie')
    sexo_nombre = serializers.ReadOnlyField(source='id_animalsexo.nombre_animalsexo')
    talla_nombre = serializers.ReadOnlyField(source='id_animaltalla.nombre_talla')
    estado_nombre = serializers.ReadOnlyField(source='id_animalestado.nombre_animalestado')
    sede_nombre = serializers.ReadOnlyField(source='id_sede.nombre_sede')

    class Meta:
        model = Animal
        fields = [
            'id_animal', 'nombre_animal', 'clave_ruac_animal', 
            'especie_nombre', 'sexo_nombre', 'talla_nombre', 
            'estado_nombre', 'sede_nombre', 'peso_animal', 
            'edad_anios_animal', 'edad_meses_animal', 
            'foto_perfil_animal', 'fecha_registro_animal'
        ]

class ExpedienteAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpedienteAnimalCompleto
        fields = '__all__'
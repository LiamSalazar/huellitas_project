from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field 
from .models import Acreedor, Cuentaporpagar, EstadoCuentasAcreedores

class AcreedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acreedor
        fields = '__all__'

class CuentaporpagarSerializer(serializers.ModelSerializer):
    acreedor_nombre = serializers.ReadOnlyField(source='id_acreedor.nombre_comercial_acreedor')
    
    esta_vencida = serializers.SerializerMethodField()

    class Meta:
        model = Cuentaporpagar
        fields = '__all__'

    @extend_schema_field(serializers.BooleanField())
    def get_esta_vencida(self, obj):
        from django.utils import timezone
        
        # USAMOS LOS NOMBRES REALES:
        estatus = obj.estado_pago
        fecha_venc = obj.fecha_vencimiento
        
        if estatus != 'Pagada' and fecha_venc:
            return fecha_venc < timezone.now().date()
        return False
    
class EstadoCuentasAcreedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCuentasAcreedores
        fields = '__all__'
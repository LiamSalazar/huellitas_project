from rest_framework import serializers
from .models import Acreedor, Cuentaporpagar, EstadoCuentasAcreedores
from apps.animals.models import Sede

class AcreedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acreedor
        fields = '__all__'

class CuentaporpagarSerializer(serializers.ModelSerializer):
    acreedor_nombre = serializers.ReadOnlyField(source='id_acreedor.nombre_comercial_acreedor')
    sede_nombre = serializers.ReadOnlyField(source='id_sede.nombre_sede')
    esta_vencida = serializers.SerializerMethodField()

    class Meta:
        model = Cuentaporpagar
        fields = '__all__' # Esto traerá el ID correcto sea cual sea su nombre

    def get_esta_vencida(self, obj):
        from django.utils import timezone
        # Verifica si el nombre del campo es estatus_pago_cuentaporpagar
        # Si en tu admin/navegador ves que se llama distinto, cámbialo aquí:
        estatus = getattr(obj, 'estatus_pago_cuentaporpagar', None)
        fecha_venc = getattr(obj, 'fecha_vencimiento_cuentaporpagar', None)
        
        if estatus != 'Pagada' and fecha_venc:
            return fecha_venc < timezone.now().date()
        return False
    
class EstadoCuentasAcreedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCuentasAcreedores
        fields = '__all__'
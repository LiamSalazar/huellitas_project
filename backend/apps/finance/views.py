from rest_framework import viewsets
from .models import Acreedor, Cuentaporpagar, EstadoCuentasAcreedores
from .serializers import AcreedorSerializer, CuentaporpagarSerializer, EstadoCuentasAcreedoresSerializer
from huellitas_config.permissions import IsDirector

class AcreedorViewSet(viewsets.ModelViewSet):
    queryset = Acreedor.objects.all()
    serializer_class = AcreedorSerializer
    permission_classes = [IsDirector] # Solo el Director puede gestionar acreedores

class CuentaporpagarViewSet(viewsets.ModelViewSet):
    queryset = Cuentaporpagar.objects.all()
    serializer_class = CuentaporpagarSerializer
    permission_classes = [IsDirector] # Solo el Director puede gestionar cuentas

    # Opcional: Filtro rápido para ver solo lo pendiente
    def get_queryset(self):
        queryset = Cuentaporpagar.objects.all()
        estatus = self.request.query_params.get('estatus')
        if estatus:
            queryset = queryset.filter(estatus_pago_cuentaporpagar=estatus)
        return queryset
    
class ReporteAcreedoresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstadoCuentasAcreedores.objects.all()
    serializer_class = EstadoCuentasAcreedoresSerializer
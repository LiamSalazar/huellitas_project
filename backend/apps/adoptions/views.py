from rest_framework import viewsets
from rest_framework import permissions as drf_permissions 
from huellitas_config import permissions as custom_permissions

from .models import Procesoadopcion, ValidarAdoptante
from .serializers import ProcesoAdopcionSerializer, ValidarAdoptanteSerializer

class ProcesoAdopcionViewSet(viewsets.ModelViewSet):
    queryset = Procesoadopcion.objects.all()
    serializer_class = ProcesoAdopcionSerializer
    
    def get_permissions(self):
        if self.action == 'destroy': # Si intentan borrar
            return [custom_permissions.permissions.IsAdminUser()] # Solo el admin/director
        return [custom_permissions.permissions.IsAuthenticated()] # Para el resto, basta estar logueado
    
class ValidarAdoptanteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ValidarAdoptante.objects.all()
    serializer_class = ValidarAdoptanteSerializer
    permission_classes = [drf_permissions.IsAuthenticated] # Voluntarios y Directores deben poder validar
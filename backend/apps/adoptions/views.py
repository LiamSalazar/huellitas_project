from rest_framework import viewsets
from rest_framework import permissions as drf_permissions 
from huellitas_config import permissions as custom_permissions

from .models import Procesoadopcion, ValidarAdoptante
from .serializers import ProcesoAdopcionSerializer, ValidarAdoptanteSerializer

class ProcesoAdopcionViewSet(viewsets.ModelViewSet):
    queryset = Procesoadopcion.objects.all()
    serializer_class = ProcesoAdopcionSerializer
    
    
class ValidarAdoptanteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ValidarAdoptante.objects.all()
    serializer_class = ValidarAdoptanteSerializer
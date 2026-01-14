from rest_framework import viewsets
from rest_framework import permissions as drf_permissions 
from huellitas_config import permissions as custom_permissions

from .serializers import AdoptanteSerializer, ProcesoAdopcionSerializer, ValidarAdoptanteSerializer

from .models import Procesoadopcion, ValidarAdoptante, Adoptante

class ProcesoAdopcionViewSet(viewsets.ModelViewSet):
    queryset = Procesoadopcion.objects.all()
    serializer_class = ProcesoAdopcionSerializer
    
    
class ValidarAdoptanteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ValidarAdoptante.objects.all()
    serializer_class = ValidarAdoptanteSerializer

class AdoptanteViewSet(viewsets.ModelViewSet):
    queryset = Adoptante.objects.all()
    serializer_class = AdoptanteSerializer
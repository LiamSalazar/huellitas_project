from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import connection # Importante para llamar al SP
from huellitas_config.permissions import IsStaffOrReadOnly
from .models import Animal, ExpedienteAnimalCompleto
from .serializers import AnimalSerializer, ExpedienteAnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsStaffOrReadOnly]

    # --- NUEVA ACCIÓN PARA EL PROCEDIMIENTO ALMACENADO ---
    @action(detail=False, methods=['post'], url_path='registrar-rescate-completo')
    def registrar_rescate_sp(self, request):
        """
        Llama al SP sp_registrar_rescate_completo para insertar 
        Dirección, Reporte y Animal en un solo paso.
        """
        d = request.data
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "CALL sp_registrar_rescate_completo(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                    [
                        # Datos Dirección
                        d.get('estado'), d.get('municipio'), d.get('calle'),
                        # Datos Animal
                        d.get('nombre'), d.get('especie_id'), d.get('sexo_id'), 
                        d.get('talla_id'), d.get('tipo_id'), d.get('funcion_id'), 
                        d.get('medio_id'), d.get('patron_id'), d.get('color_ojos_id'), 
                        d.get('color_pri_id'), d.get('caracter_id'), d.get('peso'), 
                        d.get('anios'), d.get('meses'), d.get('sede_id')
                    ]
                )
            return Response({"message": "Rescate registrado exitosamente por SQL"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ExpedienteAnimalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExpedienteAnimalCompleto.objects.all()
    serializer_class = ExpedienteAnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
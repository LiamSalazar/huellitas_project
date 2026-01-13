from rest_framework import viewsets, permissions 
from .models import Persona, Voluntario, DashboardVoluntarios
from .serializers import PersonaSerializer, VoluntarioSerializer, DashboardVoluntariosSerializer
from huellitas_config.permissions import IsDirector
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class VoluntarioViewSet(viewsets.ModelViewSet):
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer

class DashboardVoluntariosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DashboardVoluntarios.objects.all()
    serializer_class = DashboardVoluntariosSerializer
        
@csrf_exempt #Permite que el Front se conecte sin errores CSRF
def login_manual(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # En tu JS enviamos 'username' para el correo y 'password'
            email = data.get('username')
            password = data.get('password')
            
            # Buscamos en tu tabla Persona
            usuario = Persona.objects.get(email_persona=email)
            
            # Limpiamos el prefijo plain$$ si existe en la BD
            db_pass = usuario.pass_persona.replace('plain$$', '')
            
            if db_pass == password:
                return JsonResponse({
                    "status": "success",
                    "access": "token_simulado_123", 
                    "nombre": usuario.nombre_persona,
                    "id_persona": usuario.id_persona,
                    "rol": "director" 
                })
            else:
                return JsonResponse({"error": "Contraseña incorrecta"}, status=401)
                
        except Persona.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
            
    return JsonResponse({"error": "Método no permitido"}, status=405)
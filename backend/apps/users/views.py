from rest_framework import viewsets, permissions 
from .models import Persona, Voluntario, DashboardVoluntarios,  Voluntariorol  # Agregamos los modelos
from .serializers import (
    PersonaSerializer, VoluntarioSerializer, DashboardVoluntariosSerializer,
    SedeSerializer, VoluntariorolSerializer  # Agregamos los serializers
)
from apps.animals.models import Sede
from huellitas_config.permissions import IsDirector
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class VoluntarioViewSet(viewsets.ModelViewSet):
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer

# --- ESTAS SON LAS VISTAS QUE FALTABAN PARA LOS CATÁLOGOS DINÁMICOS ---

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class VoluntariorolViewSet(viewsets.ModelViewSet):
    queryset = Voluntariorol.objects.all()
    serializer_class = VoluntariorolSerializer

# -----------------------------------------------------------------------

class DashboardVoluntariosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DashboardVoluntarios.objects.all()
    serializer_class = DashboardVoluntariosSerializer

@csrf_exempt
def login_manual(request):
    # 1. Validamos que solo se acepten peticiones POST
    if request.method != 'POST':
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)
        email = data.get('username')
        password = str(data.get('password')) # Nos aseguramos de que sea string
        
        # 2. Intentamos buscar al usuario por su email
        usuario = Persona.objects.get(email_persona=email)
        
        # --- LÓGICA DE VERIFICACIÓN DE CONTRASEÑA ---
        db_password = usuario.pass_persona
        
        # Limpiamos el prefijo 'plain$$' si existe en la base de datos
        if db_password.startswith('plain$$'):
            db_password = db_password.replace('plain$$', '')

        # Comparamos: texto plano limpio O verificación de hash de Django
        if password == db_password or check_password(password, usuario.pass_persona):
            print(f"--- LOGIN EXITOSO PARA: {usuario.email_persona} (ID: {usuario.id_persona}) ---")
            # 3. Buscamos si el usuario existe en la tabla Voluntario para determinar el ROL
            voluntario_data = Voluntario.objects.filter(id_persona=usuario.id_persona).first()
            
            if usuario.email_persona == "director@huellitas.org":
                rol_asignado = "director"
            
            elif voluntario_data:    
                rol_asignado = "voluntario"
            else:
                rol_asignado = "adoptante" # Por defecto si no es voluntario ni director
            
            # 4. Respuesta exitosa con los datos necesarios para el Frontend
            return JsonResponse({
                "status": "success",
                "nombre": usuario.nombre_persona,
                "id_persona": usuario.id_persona,
                "rol": rol_asignado
            })
            
        else:
            # Si la contraseña no coincide
            print(f"DEBUG: Intento fallido para {email}. Ingresada: {password} | En BD: {usuario.pass_persona}")
            return JsonResponse({"error": "Contraseña incorrecta"}, status=401)

    except Persona.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)
    except Exception as e:
        print(f"ERROR CRÍTICO: {str(e)}")
        return JsonResponse({"error": "Error interno del servidor"}, status=500)
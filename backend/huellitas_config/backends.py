# huellitas_config/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Buscamos al usuario por su correo electrónico
            user = User.objects.get(Q(email=username))
        except User.DoesNotExist:
            return None
        
        # Si el usuario existe y la contraseña es correcta, lo dejamos pasar
        if user.check_password(password):
            return user
        return None
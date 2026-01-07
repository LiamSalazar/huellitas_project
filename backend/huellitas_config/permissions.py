# huellitas_config/permissions.py
from rest_framework import permissions

class IsDirector(permissions.BasePermission):
    """Permiso solo para el Director (Superusuario)"""
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Cualquiera puede VER (GET), pero solo el Staff 
    puede CREAR/EDITAR (POST, PATCH, DELETE).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_staff
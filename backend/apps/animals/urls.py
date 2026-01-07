from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet, ExpedienteAnimalViewSet

# El router genera automáticamente rutas para GET, POST, PUT, DELETE
router = DefaultRouter()
router.register(r'lista', AnimalViewSet, basename='animal')
router.register(r'expediente-completo', ExpedienteAnimalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
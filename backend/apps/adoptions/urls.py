from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProcesoAdopcionViewSet, ValidarAdoptanteViewSet, AdoptanteViewSet

router = DefaultRouter()
router.register(r'procesos', ProcesoAdopcionViewSet)
router.register(r'validar-adoptante', ValidarAdoptanteViewSet)
router.register(r'adoptantes', AdoptanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
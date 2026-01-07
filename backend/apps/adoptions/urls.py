from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProcesoAdopcionViewSet, ValidarAdoptanteViewSet

router = DefaultRouter()
router.register(r'procesos', ProcesoAdopcionViewSet)
router.register(r'validar-adoptante', ValidarAdoptanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
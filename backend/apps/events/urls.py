from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, EventoAsistenteViewSet

router = DefaultRouter()
router.register(r'lista', EventoViewSet)
router.register(r'asistentes', EventoAsistenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
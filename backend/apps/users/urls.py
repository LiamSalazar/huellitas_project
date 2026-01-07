from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, VoluntarioViewSet, DashboardVoluntariosViewSet

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'voluntarios', VoluntarioViewSet)
router.register(r'dashboard-voluntarios', DashboardVoluntariosViewSet, basename='dashboard-voluntarios')

urlpatterns = [
    path('', include(router.urls)),
]
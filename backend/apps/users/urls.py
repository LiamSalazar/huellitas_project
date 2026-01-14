from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, VoluntarioViewSet, DashboardVoluntariosViewSet, login_manual, SedeViewSet, VoluntariorolViewSet

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'voluntarios', VoluntarioViewSet)
router.register(r'dashboard-voluntarios', DashboardVoluntariosViewSet, basename='dashboard-voluntarios')
router.register(r'voluntariorol', VoluntariorolViewSet) 
router.register(r'sede', SedeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login-manual/', login_manual, name='login_manual'),
]
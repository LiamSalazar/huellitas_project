from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AcreedorViewSet, CuentaporpagarViewSet, ReporteAcreedoresViewSet

router = DefaultRouter()
router.register(r'acreedores', AcreedorViewSet)
router.register(r'cuentas', CuentaporpagarViewSet)
router.register(r'reporte-acreedores', ReporteAcreedoresViewSet, basename='reporte-acreedores')

urlpatterns = [
    path('', include(router.urls)),
]
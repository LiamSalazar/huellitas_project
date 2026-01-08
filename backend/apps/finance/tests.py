from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.finance.models import EstadoCuentasAcreedores

class FinanceIntegrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Creamos un Director (Superuser)
        self.director = User.objects.create_superuser(username='director', password='pass', email='d@h.com')
        # Creamos un Voluntario (Usuario normal)
        self.voluntario = User.objects.create_user(username='voluntario', password='pass')

    def test_reporte_acreedores_accesibilidad(self):
        """Verifica que la vista SQL devuelva datos al director"""
        self.client.force_authenticate(user=self.director)
        response = self.client.get('/api/finance/reporte-acreedores/')
        # Si la vista SQL está vacía, devuelve 200 con lista vacía. Si falla el SQL, da 500.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_seguridad_reporte_acreedores(self):
        """PRUEBA RIGUROSA: El voluntario NO debe ver finanzas"""
        self.client.force_authenticate(user=self.voluntario)
        response = self.client.get('/api/finance/reporte-acreedores/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
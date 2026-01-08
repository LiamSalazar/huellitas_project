from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class EventsIntegrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='staff', password='pass123')

    def test_lista_eventos_publica(self):
        """Verifica que cualquier usuario pueda ver el calendario de eventos"""
        response = self.client.get('/api/events/lista/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_registro_asistente_protegido(self):
        """Verifica que no se puedan gestionar asistentes sin login"""
        response = self.client.get('/api/events/asistentes/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
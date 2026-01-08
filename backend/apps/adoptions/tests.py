from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class AdoptionsRigorousTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_endpoint_validacion_requiere_auth(self):
        """PRUEBA DE FUEGO: Nadie puede validar adoptantes sin estar logueado"""
        response = self.client.get('/api/adoptions/validar-adoptante/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
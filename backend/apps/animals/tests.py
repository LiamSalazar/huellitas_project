from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class AnimalsPublicTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_expediente_publico_accesible(self):
        """El frontend debe poder ver animales sin token"""
        response = self.client.get('/api/animals/expediente-completo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verificamos que sea una lista lo que llega
        self.assertIsInstance(response.data, list)
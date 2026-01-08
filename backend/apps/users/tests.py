from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class UserAuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(
            username=self.username, 
            password=self.password,
            email='test@huellitas.com'
        )

    def test_login_obtener_token(self):
        """Verifica que el login devuelva tokens JWT"""
        response = self.client.post('/api/token/', {
            'username': self.username,
            'password': self.password
        }, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_acceso_con_token_valido(self):
        """Prueba que el token realmente sirva para entrar a una ruta protegida"""
        # 1. Login
        login_res = self.client.post('/api/token/', {
            'username': self.username,
            'password': self.password
        })
        token = login_res.data['access']
        
        # 2. Intentar acceder con Header de Autorización
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        # Usamos una ruta que sabemos que existe
        response = self.client.get('/api/users/dashboard-voluntarios/') 
        
        # Si el token es bueno, no debería dar 401
        self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_credenciales_invalidas(self):
        """Asegura que no deje entrar con datos falsos"""
        response = self.client.post('/api/token/', {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
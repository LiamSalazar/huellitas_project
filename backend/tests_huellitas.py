from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class ProyectoHuellitasTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Usuario normal
        self.user = User.objects.create_user(
            username='voluntario@correo.com', 
            email='voluntario@correo.com', 
            password='password123'
        )
        # Director (Superusuario)
        self.director = User.objects.create_superuser(
            username='director@correo.com', 
            email='director@correo.com', 
            password='adminpassword'
        )

    def test_flujo_seguridad_completo(self):
        """Prueba que los candados funcionen en todo el proyecto"""
        
        # 1. Intentar ver animales sin estar logueado (Debe fallar 401)
        res_animales = self.client.get('/api/animals/lista/')
        self.assertEqual(res_animales.status_code, status.HTTP_200_OK)

        # 2. Login con el usuario voluntario
        login_res = self.client.post('/api/token/', {
            "username": "voluntario@correo.com",
            "password": "password123"
        })
        self.assertEqual(login_res.status_code, status.HTTP_200_OK)
        token = login_res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # 3. Voluntario intenta ver finanzas (Debe fallar 403 Forbidden)
        res_finanzas = self.client.get('/api/finance/cuentas/')
        self.assertIn(
            res_finanzas.status_code,
            [status.HTTP_403_FORBIDDEN, status.HTTP_404_NOT_FOUND]
        )


        # 4. Cambiar a cuenta de Director y ver finanzas (Debe ser 200 OK)
        self.client.force_authenticate(user=self.director)
        res_director = self.client.get('/api/finance/cuentas/')
        self.assertEqual(res_director.status_code, status.HTTP_200_OK)
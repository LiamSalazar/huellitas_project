from django.test import TestCase
from apps.finance.serializers import CuentaporpagarSerializer
from datetime import date, timedelta

class LogicBusinessTests(TestCase):
    def test_logica_cuentas_vencidas(self):
        """Verifica que el cálculo de vencimiento sea exacto"""
        serializer = CuentaporpagarSerializer()
        
        # Mock de una cuenta vencida
        class CuentaVencida:
            estado_pago = 'Pendiente'
            fecha_vencimiento = date.today() - timedelta(days=5)
            
        # Mock de una cuenta pagada (aunque la fecha sea vieja, no debe estar vencida)
        class CuentaPagada:
            estado_pago = 'Pagada'
            fecha_vencimiento = date.today() - timedelta(days=5)

        self.assertTrue(serializer.get_esta_vencida(CuentaVencida()))
        self.assertFalse(serializer.get_esta_vencida(CuentaPagada()))
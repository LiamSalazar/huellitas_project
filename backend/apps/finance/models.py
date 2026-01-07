# (requiere Django >= 5.2)

from django.db import models


class Acreedor(models.Model):
    id_acreedor = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('users.Persona', models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    nombre_comercial_acreedor = models.CharField(max_length=150)
    rfc_acreedor = models.CharField(unique=True, max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Acreedor'


class Cuentaporpagar(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    id_acreedor = models.ForeignKey('finance.Acreedor', models.DO_NOTHING, db_column='id_acreedor')
    monto_original = models.DecimalField(max_digits=10, decimal_places=2)
    monto_abonado = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    concepto_deuda = models.TextField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    estado_pago = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'CuentaPorPagar'


class Donacion(models.Model):
    id_donacion = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('users.Persona', models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    monto_donacion = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_donacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Donacion'

class EstadoCuentasAcreedores(models.Model):
    # nombre_Comercial_Acreedor como PK para que Django funcione
    nombre_comercial_acreedor = models.CharField(max_length=255, primary_key=True, db_column='nombre_comercial_acreedor')
    rfc_acreedor = models.CharField(max_length=20, db_column='rfc_acreedor')
    concepto_deuda = models.CharField(max_length=255, db_column='concepto_deuda')
    monto_original = models.DecimalField(max_digits=12, decimal_places=2, db_column='monto_original')
    monto_abonado = models.DecimalField(max_digits=12, decimal_places=2, db_column='monto_abonado')
    saldo_pendiente = models.DecimalField(max_digits=12, decimal_places=2, db_column='saldo_pendiente')
    fecha_vencimiento = models.DateField(db_column='fecha_vencimiento')
    estado_pago = models.CharField(max_length=50, db_column='estado_pago')
    estatus_vencimiento = models.CharField(max_length=20, db_column='estatus_vencimiento')

    class Meta:
        managed = False
        db_table = 'vw_EstadoCuentasAcreedores'
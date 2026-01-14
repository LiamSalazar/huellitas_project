# (requiere Django >= 5.2)

from django.db import models


class Blacklistmotivo(models.Model):
    id_blacklistmotivo = models.AutoField(primary_key=True)
    nombre_blacklistmotivo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'BlacklistMotivo'


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    estado_direccion = models.CharField(max_length=80)
    municipio_direccion = models.CharField(max_length=120)
    colonia_direccion = models.CharField(max_length=120, blank=True, null=True)
    calle_direccion = models.CharField(max_length=120, blank=True, null=True)
    numero_exterior_direccion = models.CharField(max_length=30, blank=True, null=True)
    numero_interior_direccion = models.CharField(max_length=30, blank=True, null=True)
    codigo_postal_direccion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Direccion'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre_persona = models.CharField(max_length=120)
    apellidos_persona = models.CharField(max_length=120)
    telefono_persona = models.CharField(max_length=20)
    email_persona = models.CharField(unique=True, max_length=120)
    pass_persona = models.CharField(max_length=255)
    id_direccion = models.ForeignKey('users.Direccion', models.DO_NOTHING, db_column='id_direccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Persona'


class Personablacklist(models.Model):
    id_personablacklist = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('users.Persona', models.DO_NOTHING, db_column='id_persona')
    id_blacklistmotivo = models.ForeignKey('users.Blacklistmotivo', models.DO_NOTHING, db_column='id_blacklistmotivo')
    fecha_incidente = models.DateTimeField()
    detalle_incidente = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PersonaBlacklist'


class Personasexo(models.Model):
    id_personasexo = models.AutoField(primary_key=True)
    nombre_personasexo = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'PersonaSexo'


class Voluntario(models.Model):
    id_voluntario = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField('users.Persona', models.DO_NOTHING, db_column='id_persona')
    id_voluntariorol = models.ForeignKey('users.Voluntariorol', models.DO_NOTHING, db_column='id_voluntariorol')
    cedula_profesional_voluntario = models.CharField(max_length=30, blank=True, null=True)
    # upload_to crea las subcarpetas dentro de 'media' automáticamente
    ruta_ine_voluntario = models.FileField(
        upload_to='voluntarios/ine/', 
        max_length=300,
        null=True, # Permite que esté vacío en la BD
        blank=True # Permite que el formulario lo envíe vacío
    )
    
    ruta_carta_compromiso_voluntario = models.FileField(
        upload_to='voluntarios/cartas/', 
        max_length=300,
        null=True, 
        blank=True
    )


    class Meta:
        managed = False
        db_table = 'Voluntario'


class Voluntarioasistencia(models.Model):
    pk = models.CompositePrimaryKey('id_voluntario', 'id_sede', 'entrada')
    id_voluntario = models.ForeignKey('users.Voluntario', models.DO_NOTHING, db_column='id_voluntario')
    id_sede = models.ForeignKey('animals.Sede', models.DO_NOTHING, db_column='id_sede')
    entrada = models.DateTimeField()
    salida = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VoluntarioAsistencia'


class Voluntariorol(models.Model):
    id_voluntariorol = models.AutoField(primary_key=True)
    nombre_voluntariorol = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'VoluntarioRol'


class Voluntariosedeasignacion(models.Model):
    pk = models.CompositePrimaryKey('id_voluntario', 'id_sede', 'fecha_inicio')
    id_voluntario = models.ForeignKey('users.Voluntario', models.DO_NOTHING, db_column='id_voluntario')
    id_sede = models.ForeignKey('animals.Sede', models.DO_NOTHING, db_column='id_sede')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VoluntarioSedeAsignacion'

class DashboardVoluntarios(models.Model):
    # Usamos id_voluntario como Primary Key
    id_voluntario = models.IntegerField(primary_key=True, db_column='id_voluntario')
    nombre_completo = models.CharField(max_length=255, db_column='nombre_completo')
    rol = models.CharField(max_length=100, db_column='rol')
    sede_actual = models.CharField(max_length=100, db_column='sede_actual')
    # Este campo puede ser nulo si el voluntario nunca ha marcado entrada
    ultima_entrada_activa = models.DateTimeField(null=True, blank=True, db_column='ultima_entrada_activa')

    class Meta:
        managed = False  # No tocar la BD real
        db_table = 'vw_DashboardVoluntarios'
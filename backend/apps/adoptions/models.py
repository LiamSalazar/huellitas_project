# requiere Django >= 5.2)

from django.db import models


class Adoptante(models.Model):
    id_adoptante = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField('users.Persona', models.DO_NOTHING, db_column='id_persona')
    id_viviendatipo = models.ForeignKey('adoptions.Viviendatipo', models.DO_NOTHING, db_column='id_viviendatipo')
    metros_vivienda_adoptante = models.SmallIntegerField()
    patio_adoptante = models.BooleanField()
    tiene_perros_adoptante = models.BooleanField()
    tiene_gatos_adoptante = models.BooleanField()
    ocupacion_adoptante = models.CharField(max_length=120, blank=True, null=True)
    edad_adoptante = models.SmallIntegerField()
    id_personasexo = models.ForeignKey('users.Personasexo', models.DO_NOTHING, db_column='id_personasexo')
    hijos_pequenos_adoptante = models.BooleanField()
    id_adoptanteniveleconomico = models.ForeignKey('adoptions.Adoptanteniveleconomico', models.DO_NOTHING, db_column='id_adoptanteniveleconomico')
    ruta_identificacion_adoptante = models.CharField(max_length=300, blank=True, null=True)
    ruta_comprobante_domicilio_adoptante = models.CharField(max_length=300, blank=True, null=True)
    ruta_responsiva_adoptante = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Adoptante'


class Adoptanteniveleconomico(models.Model):
    id_adoptanteniveleconomico = models.AutoField(primary_key=True)
    nombre_adoptanteniveleconomico = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'AdoptanteNivelEconomico'


class Animalantecedente(models.Model):
    pk = models.CompositePrimaryKey('id_animal', 'id_antecedentecatalogo')
    id_animal = models.ForeignKey('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    id_antecedentecatalogo = models.ForeignKey('animals.Antecedentecatalogo', models.DO_NOTHING, db_column='id_antecedentecatalogo')

    class Meta:
        managed = False
        db_table = 'AnimalAntecedente'


class Animalvacuna(models.Model):
    pk = models.CompositePrimaryKey('id_animal', 'id_vacunacatalogo', 'fecha_aplicacion')
    id_animal = models.ForeignKey('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    id_vacunacatalogo = models.ForeignKey('animals.Vacunacatalogo', models.DO_NOTHING, db_column='id_vacunacatalogo')
    fecha_aplicacion = models.DateField()
    fecha_refuerzo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AnimalVacuna'


class Colorcombinacion(models.Model):
    pk = models.CompositePrimaryKey('id_animal', 'id_colorprincipal')
    id_animal = models.ForeignKey('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    id_colorprincipal = models.ForeignKey('animals.Colorprincipal', models.DO_NOTHING, db_column='id_colorprincipal')

    class Meta:
        managed = False
        db_table = 'ColorCombinacion'


class Procesoadopcion(models.Model):
    id_procesoadopcion = models.AutoField(primary_key=True)
    id_animal = models.OneToOneField('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    id_adoptante = models.ForeignKey('adoptions.Adoptante', models.DO_NOTHING, db_column='id_adoptante')
    id_voluntario = models.ForeignKey('users.Voluntario', models.DO_NOTHING, db_column='id_voluntario', blank=True, null=True)
    id_procesoadopcionestado = models.ForeignKey('adoptions.Procesoadopcionestado', models.DO_NOTHING, db_column='id_procesoadopcionestado')
    fecha_inicio_proceso = models.DateTimeField()
    fecha_cierre_proceso = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProcesoAdopcion'


class Procesoadopcioncita(models.Model):
    id_procesoadopcion = models.OneToOneField('adoptions.Procesoadopcion', models.DO_NOTHING, db_column='id_procesoadopcion', primary_key=True)
    fecha_hora_cita = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ProcesoAdopcionCita'


class Procesoadopcionestado(models.Model):
    id_procesoadopcionestado = models.AutoField(primary_key=True)
    nombre_procesoadopcionestado = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'ProcesoAdopcionEstado'


class Retiromascota(models.Model):
    id_retiromascota = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('users.Persona', models.DO_NOTHING, db_column='id_persona')
    id_animal = models.ForeignKey('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    fecha_retiro = models.DateTimeField()
    id_blacklistmotivo = models.ForeignKey('users.Blacklistmotivo', models.DO_NOTHING, db_column='id_blacklistmotivo')

    class Meta:
        managed = False
        db_table = 'RetiroMascota'


class Viviendatipo(models.Model):
    id_viviendatipo = models.AutoField(primary_key=True)
    nombre_viviendatipo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'ViviendaTipo'

class ValidarAdoptante(models.Model):
    id_persona = models.IntegerField(primary_key=True, db_column='id_persona')
    nombre = models.CharField(max_length=255, db_column='nombre')
    esta_en_blacklist = models.BooleanField(db_column='esta_en_blacklist')
    procesos_activos_totales = models.IntegerField(db_column='procesos_activos_totales')

    class Meta:
        managed = False
        db_table = 'vw_ValidarAdoptante'
# (requiere Django >= 5.2)

from django.db import models


class Alergiacatalogo(models.Model):
    id_alergiacatalogo = models.AutoField(primary_key=True)
    nombre_alergiacatalogo = models.CharField(unique=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'AlergiaCatalogo'


class Animal(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nombre_animal = models.CharField(max_length=120)
    clave_ruac_animal = models.CharField(unique=True, max_length=50, blank=True, null=True)
    id_animalespecie = models.ForeignKey('animals.Animalespecie', models.DO_NOTHING, db_column='id_animalespecie')
    id_animalsexo = models.ForeignKey('animals.Animalsexo', models.DO_NOTHING, db_column='id_animalsexo')
    id_animaltalla = models.ForeignKey('animals.Animaltalla', models.DO_NOTHING, db_column='id_animaltalla')
    id_animaltipo = models.ForeignKey('animals.Animaltipo', models.DO_NOTHING, db_column='id_animaltipo')
    id_animalfuncion = models.ForeignKey('animals.Animalfuncion', models.DO_NOTHING, db_column='id_animalfuncion')
    id_mediollegada = models.ForeignKey('animals.Mediollegada', models.DO_NOTHING, db_column='id_mediollegada')
    id_patronpelaje = models.ForeignKey('animals.Patronpelaje', models.DO_NOTHING, db_column='id_patronpelaje')
    id_colorojos = models.ForeignKey('animals.Colorojos', models.DO_NOTHING, db_column='id_colorojos')
    id_colorprincipal = models.ForeignKey('animals.Colorprincipal', models.DO_NOTHING, db_column='id_colorprincipal')
    id_razaperro = models.ForeignKey('animals.Razaperro', models.DO_NOTHING, db_column='id_razaperro', blank=True, null=True)
    id_razagato = models.ForeignKey('animals.Razagato', models.DO_NOTHING, db_column='id_razagato', blank=True, null=True)
    id_animalcaracter = models.ForeignKey('animals.Animalcaracter', models.DO_NOTHING, db_column='id_animalcaracter')
    id_animalestado = models.ForeignKey('animals.Animalestado', models.DO_NOTHING, db_column='id_animalestado')
    peso_animal = models.DecimalField(max_digits=5, decimal_places=2)
    edad_anios_animal = models.SmallIntegerField()
    edad_meses_animal = models.SmallIntegerField()
    foto_perfil_animal = models.CharField(max_length=300, blank=True, null=True)
    fecha_registro_animal = models.DateTimeField()
    id_sede = models.ForeignKey('animals.Sede', models.DO_NOTHING, db_column='id_sede', blank=True, null=True)
    id_reporteanimal = models.ForeignKey('animals.Reporteanimal', models.DO_NOTHING, db_column='id_reporteanimal', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Animal'


class Animalalergia(models.Model):
    pk = models.CompositePrimaryKey('id_animal', 'id_alergiacatalogo')
    id_animal = models.ForeignKey('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    id_alergiacatalogo = models.ForeignKey('animals.Alergiacatalogo', models.DO_NOTHING, db_column='id_alergiacatalogo')

    class Meta:
        managed = False
        db_table = 'AnimalAlergia'


class Animalcaracter(models.Model):
    id_animalcaracter = models.AutoField(primary_key=True)
    nombre_animalcaracter = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'AnimalCaracter'


class Animalespecie(models.Model):
    id_animalespecie = models.AutoField(primary_key=True)
    nombre_animalespecie = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'AnimalEspecie'


class Animalestado(models.Model):
    id_animalestado = models.AutoField(primary_key=True)
    nombre_animalestado = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'AnimalEstado'


class Animalfuncion(models.Model):
    id_animalfuncion = models.AutoField(primary_key=True)
    nombre_animalfuncion = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'AnimalFuncion'


class Animalpadecimiento(models.Model):
    pk = models.CompositePrimaryKey('id_animal', 'id_padecimientocatalogo')
    id_animal = models.ForeignKey('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    id_padecimientocatalogo = models.ForeignKey('animals.Padecimientocatalogo', models.DO_NOTHING, db_column='id_padecimientocatalogo')

    class Meta:
        managed = False
        db_table = 'AnimalPadecimiento'


class Animalsexo(models.Model):
    id_animalsexo = models.AutoField(primary_key=True)
    nombre_animalsexo = models.CharField(unique=True, max_length=12)

    class Meta:
        managed = False
        db_table = 'AnimalSexo'


class Animaltalla(models.Model):
    id_animaltalla = models.AutoField(primary_key=True)
    nombre_talla = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'AnimalTalla'


class Animaltipo(models.Model):
    id_animaltipo = models.AutoField(primary_key=True)
    nombre_animaltipo = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'AnimalTipo'


class Antecedentecatalogo(models.Model):
    id_antecedentecatalogo = models.AutoField(primary_key=True)
    nombre_antecedentecatalogo = models.CharField(unique=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'AntecedenteCatalogo'


class Colorojos(models.Model):
    id_colorojos = models.AutoField(primary_key=True)
    nombre_colorojos = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'ColorOjos'


class Colorprincipal(models.Model):
    id_colorprincipal = models.AutoField(primary_key=True)
    nombre_colorprincipal = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'ColorPrincipal'


class Fotografia(models.Model):
    id_fotografia = models.AutoField(primary_key=True)
    id_animal = models.ForeignKey('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    ruta_archivo_fotografia = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'Fotografia'


class Identificadoranimal(models.Model):
    id_identificadoranimal = models.AutoField(primary_key=True)
    id_animal = models.OneToOneField('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    id_identificadortipo = models.ForeignKey('animals.Identificadortipo', models.DO_NOTHING, db_column='id_identificadortipo')
    valor_identificadoranimal = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'IdentificadorAnimal'


class Identificadortipo(models.Model):
    id_identificadortipo = models.AutoField(primary_key=True)
    nombre_identificadortipo = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'IdentificadorTipo'


class Mediollegada(models.Model):
    id_mediollegada = models.AutoField(primary_key=True)
    nombre_mediollegada = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'MedioLlegada'


class Padecimientocatalogo(models.Model):
    id_padecimientocatalogo = models.AutoField(primary_key=True)
    nombre_padecimientocatalogo = models.CharField(unique=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'PadecimientoCatalogo'


class Patronpelaje(models.Model):
    id_patronpelaje = models.AutoField(primary_key=True)
    nombre_patronpelaje = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'PatronPelaje'


class Razagato(models.Model):
    id_razagato = models.AutoField(primary_key=True)
    nombre_razagato = models.CharField(unique=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'RazaGato'


class Razaperro(models.Model):
    id_razaperro = models.AutoField(primary_key=True)
    nombre_razaperro = models.CharField(unique=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'RazaPerro'


class Reporteanimal(models.Model):
    id_reporteanimal = models.AutoField(primary_key=True)
    id_direccion = models.ForeignKey('users.Direccion', models.DO_NOTHING, db_column='id_direccion')
    id_colorprincipal = models.ForeignKey('animals.Colorprincipal', models.DO_NOTHING, db_column='id_colorprincipal', blank=True, null=True)
    id_colorojos = models.ForeignKey('animals.Colorojos', models.DO_NOTHING, db_column='id_colorojos', blank=True, null=True)
    telefono_reportante = models.CharField(max_length=20, blank=True, null=True)
    ruta_foto_reporteanimal = models.CharField(max_length=300, blank=True, null=True)
    fecha_reporteanimal = models.DateTimeField()
    id_voluntarioasignado = models.ForeignKey('users.Voluntario', models.DO_NOTHING, db_column='id_voluntarioasignado', blank=True, null=True)
    id_sededestino = models.ForeignKey('animals.Sede', models.DO_NOTHING, db_column='id_sededestino', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ReporteAnimal'


class Reportecolorcombinacion(models.Model):
    pk = models.CompositePrimaryKey('id_reporteanimal', 'id_colorprincipal')
    id_reporteanimal = models.ForeignKey('animals.Reporteanimal', models.DO_NOTHING, db_column='id_reporteanimal')
    id_colorprincipal = models.ForeignKey('animals.Colorprincipal', models.DO_NOTHING, db_column='id_colorprincipal')

    class Meta:
        managed = False
        db_table = 'ReporteColorCombinacion'


class Saludanimal(models.Model):
    id_saludanimal = models.AutoField(primary_key=True)
    id_animal = models.OneToOneField('animals.Animal', models.DO_NOTHING, db_column='id_animal')
    fecha_esterilizacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SaludAnimal'


class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(unique=True, max_length=120)
    id_direccion = models.ForeignKey('users.Direccion', models.DO_NOTHING, db_column='id_direccion')

    class Meta:
        managed = False
        db_table = 'Sede'


class Vacunacatalogo(models.Model):
    id_vacunacatalogo = models.AutoField(primary_key=True)
    nombre_vacunacatalogo = models.CharField(unique=True, max_length=120)
    dias_vigencia_vacunacatalogo = models.IntegerField()
    dias_refuerzo_vacunacatalogo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VacunaCatalogo'

class ExpedienteAnimalCompleto(models.Model):
    id_animal = models.IntegerField(primary_key=True, db_column='id_animal')
    nombre_animal = models.CharField(max_length=255, db_column='nombre_animal')
    clave_ruac_animal = models.CharField(max_length=50, db_column='clave_ruac_animal')
    especie = models.CharField(max_length=100, db_column='especie')
    sexo = models.CharField(max_length=50, db_column='sexo')
    raza = models.CharField(max_length=100, db_column='raza')
    talla = models.CharField(max_length=50, db_column='talla')
    tipo = models.CharField(max_length=100, db_column='tipo')
    peso_animal = models.DecimalField(max_digits=5, decimal_places=2, db_column='peso_animal')
    edad_formateada = models.CharField(max_length=100, db_column='edad_formateada')
    sede_actual = models.CharField(max_length=100, db_column='sede_actual')
    total_fotos = models.IntegerField(db_column='total_fotos')

    class Meta:
        managed = False
        db_table = 'vw_ExpedienteAnimalCompleto'
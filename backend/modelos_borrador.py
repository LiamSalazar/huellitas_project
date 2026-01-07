#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acreedor(models.Model):
    id_acreedor = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    nombre_comercial_acreedor = models.CharField(max_length=150)
    rfc_acreedor = models.CharField(unique=True, max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Acreedor'


class Adoptante(models.Model):
    id_adoptante = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id_persona')
    id_viviendatipo = models.ForeignKey('Viviendatipo', models.DO_NOTHING, db_column='id_viviendatipo')
    metros_vivienda_adoptante = models.SmallIntegerField()
    patio_adoptante = models.BooleanField()
    tiene_perros_adoptante = models.BooleanField()
    tiene_gatos_adoptante = models.BooleanField()
    ocupacion_adoptante = models.CharField(max_length=120, blank=True, null=True)
    edad_adoptante = models.SmallIntegerField()
    id_personasexo = models.ForeignKey('Personasexo', models.DO_NOTHING, db_column='id_personasexo')
    hijos_pequenos_adoptante = models.BooleanField()
    id_adoptanteniveleconomico = models.ForeignKey('Adoptanteniveleconomico', models.DO_NOTHING, db_column='id_adoptanteniveleconomico')
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
    id_animalespecie = models.ForeignKey('Animalespecie', models.DO_NOTHING, db_column='id_animalespecie')
    id_animalsexo = models.ForeignKey('Animalsexo', models.DO_NOTHING, db_column='id_animalsexo')
    id_animaltalla = models.ForeignKey('Animaltalla', models.DO_NOTHING, db_column='id_animaltalla')
    id_animaltipo = models.ForeignKey('Animaltipo', models.DO_NOTHING, db_column='id_animaltipo')
    id_animalfuncion = models.ForeignKey('Animalfuncion', models.DO_NOTHING, db_column='id_animalfuncion')
    id_mediollegada = models.ForeignKey('Mediollegada', models.DO_NOTHING, db_column='id_mediollegada')
    id_patronpelaje = models.ForeignKey('Patronpelaje', models.DO_NOTHING, db_column='id_patronpelaje')
    id_colorojos = models.ForeignKey('Colorojos', models.DO_NOTHING, db_column='id_colorojos')
    id_colorprincipal = models.ForeignKey('Colorprincipal', models.DO_NOTHING, db_column='id_colorprincipal')
    id_razaperro = models.ForeignKey('Razaperro', models.DO_NOTHING, db_column='id_razaperro', blank=True, null=True)
    id_razagato = models.ForeignKey('Razagato', models.DO_NOTHING, db_column='id_razagato', blank=True, null=True)
    id_animalcaracter = models.ForeignKey('Animalcaracter', models.DO_NOTHING, db_column='id_animalcaracter')
    id_animalestado = models.ForeignKey('Animalestado', models.DO_NOTHING, db_column='id_animalestado')
    peso_animal = models.DecimalField(max_digits=5, decimal_places=2)
    edad_anios_animal = models.SmallIntegerField()
    edad_meses_animal = models.SmallIntegerField()
    foto_perfil_animal = models.CharField(max_length=300, blank=True, null=True)
    fecha_registro_animal = models.DateTimeField()
    id_sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='id_sede', blank=True, null=True)
    id_reporteanimal = models.ForeignKey('Reporteanimal', models.DO_NOTHING, db_column='id_reporteanimal', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Animal'


class Animalalergia(models.Model):
    pk = models.CompositePrimaryKey('id_animal', 'id_alergiacatalogo')
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')
    id_alergiacatalogo = models.ForeignKey(Alergiacatalogo, models.DO_NOTHING, db_column='id_alergiacatalogo')

    class Meta:
        managed = False
        db_table = 'AnimalAlergia'


class Animalantecedente(models.Model):
    pk = models.CompositePrimaryKey('id_animal', 'id_antecedentecatalogo')
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')
    id_antecedentecatalogo = models.ForeignKey('Antecedentecatalogo', models.DO_NOTHING, db_column='id_antecedentecatalogo')

    class Meta:
        managed = False
        db_table = 'AnimalAntecedente'


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
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')
    id_padecimientocatalogo = models.ForeignKey('Padecimientocatalogo', models.DO_NOTHING, db_column='id_padecimientocatalogo')

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


class Animalvacuna(models.Model):
    pk = models.CompositePrimaryKey('id_animal', 'id_vacunacatalogo', 'fecha_aplicacion')
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')
    id_vacunacatalogo = models.ForeignKey('Vacunacatalogo', models.DO_NOTHING, db_column='id_vacunacatalogo')
    fecha_aplicacion = models.DateField()
    fecha_refuerzo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AnimalVacuna'


class Antecedentecatalogo(models.Model):
    id_antecedentecatalogo = models.AutoField(primary_key=True)
    nombre_antecedentecatalogo = models.CharField(unique=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'AntecedenteCatalogo'


class Blacklistmotivo(models.Model):
    id_blacklistmotivo = models.AutoField(primary_key=True)
    nombre_blacklistmotivo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'BlacklistMotivo'


class Colorcombinacion(models.Model):
    pk = models.CompositePrimaryKey('id_animal', 'id_colorprincipal')
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')
    id_colorprincipal = models.ForeignKey('Colorprincipal', models.DO_NOTHING, db_column='id_colorprincipal')

    class Meta:
        managed = False
        db_table = 'ColorCombinacion'


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


class Cuentaporpagar(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    id_acreedor = models.ForeignKey(Acreedor, models.DO_NOTHING, db_column='id_acreedor')
    monto_original = models.DecimalField(max_digits=10, decimal_places=2)
    monto_abonado = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    concepto_deuda = models.TextField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    estado_pago = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'CuentaPorPagar'


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


class Donacion(models.Model):
    id_donacion = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    monto_donacion = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_donacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Donacion'


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    titulo_evento = models.CharField(max_length=200)
    descripcion_evento = models.TextField()
    id_eventotipo = models.ForeignKey('Eventotipo', models.DO_NOTHING, db_column='id_eventotipo')
    id_sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='id_sede')
    fecha_inicio_evento = models.DateTimeField()
    fecha_fin_evento = models.DateTimeField()
    cupo_maximo_evento = models.IntegerField(blank=True, null=True)
    id_voluntarioorganizador = models.ForeignKey('Voluntario', models.DO_NOTHING, db_column='id_voluntarioorganizador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Evento'


class Eventoasistente(models.Model):
    pk = models.CompositePrimaryKey('id_evento', 'id_persona')
    id_evento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='id_evento')
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')

    class Meta:
        managed = False
        db_table = 'EventoAsistente'


class Eventotipo(models.Model):
    id_eventotipo = models.AutoField(primary_key=True)
    nombre_eventotipo = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'EventoTipo'


class Fotografia(models.Model):
    id_fotografia = models.AutoField(primary_key=True)
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')
    ruta_archivo_fotografia = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'Fotografia'


class Identificadoranimal(models.Model):
    id_identificadoranimal = models.AutoField(primary_key=True)
    id_animal = models.OneToOneField(Animal, models.DO_NOTHING, db_column='id_animal')
    id_identificadortipo = models.ForeignKey('Identificadortipo', models.DO_NOTHING, db_column='id_identificadortipo')
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


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre_persona = models.CharField(max_length=120)
    apellidos_persona = models.CharField(max_length=120)
    telefono_persona = models.CharField(max_length=20)
    email_persona = models.CharField(unique=True, max_length=120)
    pass_persona = models.CharField(max_length=255)
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Persona'


class Personablacklist(models.Model):
    id_personablacklist = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')
    id_blacklistmotivo = models.ForeignKey(Blacklistmotivo, models.DO_NOTHING, db_column='id_blacklistmotivo')
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


class Procesoadopcion(models.Model):
    id_procesoadopcion = models.AutoField(primary_key=True)
    id_animal = models.OneToOneField(Animal, models.DO_NOTHING, db_column='id_animal')
    id_adoptante = models.ForeignKey(Adoptante, models.DO_NOTHING, db_column='id_adoptante')
    id_voluntario = models.ForeignKey('Voluntario', models.DO_NOTHING, db_column='id_voluntario', blank=True, null=True)
    id_procesoadopcionestado = models.ForeignKey('Procesoadopcionestado', models.DO_NOTHING, db_column='id_procesoadopcionestado')
    fecha_inicio_proceso = models.DateTimeField()
    fecha_cierre_proceso = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProcesoAdopcion'


class Procesoadopcioncita(models.Model):
    id_procesoadopcion = models.OneToOneField(Procesoadopcion, models.DO_NOTHING, db_column='id_procesoadopcion', primary_key=True)
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
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion')
    id_colorprincipal = models.ForeignKey(Colorprincipal, models.DO_NOTHING, db_column='id_colorprincipal', blank=True, null=True)
    id_colorojos = models.ForeignKey(Colorojos, models.DO_NOTHING, db_column='id_colorojos', blank=True, null=True)
    telefono_reportante = models.CharField(max_length=20, blank=True, null=True)
    ruta_foto_reporteanimal = models.CharField(max_length=300, blank=True, null=True)
    fecha_reporteanimal = models.DateTimeField()
    id_voluntarioasignado = models.ForeignKey('Voluntario', models.DO_NOTHING, db_column='id_voluntarioasignado', blank=True, null=True)
    id_sededestino = models.ForeignKey('Sede', models.DO_NOTHING, db_column='id_sededestino', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ReporteAnimal'


class Reportecolorcombinacion(models.Model):
    pk = models.CompositePrimaryKey('id_reporteanimal', 'id_colorprincipal')
    id_reporteanimal = models.ForeignKey(Reporteanimal, models.DO_NOTHING, db_column='id_reporteanimal')
    id_colorprincipal = models.ForeignKey(Colorprincipal, models.DO_NOTHING, db_column='id_colorprincipal')

    class Meta:
        managed = False
        db_table = 'ReporteColorCombinacion'


class Retiromascota(models.Model):
    id_retiromascota = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')
    id_animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='id_animal')
    fecha_retiro = models.DateTimeField()
    id_blacklistmotivo = models.ForeignKey(Blacklistmotivo, models.DO_NOTHING, db_column='id_blacklistmotivo')

    class Meta:
        managed = False
        db_table = 'RetiroMascota'


class Saludanimal(models.Model):
    id_saludanimal = models.AutoField(primary_key=True)
    id_animal = models.OneToOneField(Animal, models.DO_NOTHING, db_column='id_animal')
    fecha_esterilizacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SaludAnimal'


class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(unique=True, max_length=120)
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion')

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


class Viviendatipo(models.Model):
    id_viviendatipo = models.AutoField(primary_key=True)
    nombre_viviendatipo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'ViviendaTipo'


class Voluntario(models.Model):
    id_voluntario = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='id_persona')
    id_voluntariorol = models.ForeignKey('Voluntariorol', models.DO_NOTHING, db_column='id_voluntariorol')
    cedula_profesional_voluntario = models.CharField(max_length=30, blank=True, null=True)
    ruta_ine_voluntario = models.CharField(max_length=300)
    ruta_carta_compromiso_voluntario = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'Voluntario'


class Voluntarioasistencia(models.Model):
    pk = models.CompositePrimaryKey('id_voluntario', 'id_sede', 'entrada')
    id_voluntario = models.ForeignKey(Voluntario, models.DO_NOTHING, db_column='id_voluntario')
    id_sede = models.ForeignKey(Sede, models.DO_NOTHING, db_column='id_sede')
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
    id_voluntario = models.ForeignKey(Voluntario, models.DO_NOTHING, db_column='id_voluntario')
    id_sede = models.ForeignKey(Sede, models.DO_NOTHING, db_column='id_sede')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VoluntarioSedeAsignacion'

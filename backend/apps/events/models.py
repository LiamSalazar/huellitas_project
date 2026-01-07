# (requiere Django >= 5.2)

from django.db import models


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    titulo_evento = models.CharField(max_length=200)
    descripcion_evento = models.TextField()
    id_eventotipo = models.ForeignKey('events.Eventotipo', models.DO_NOTHING, db_column='id_eventotipo')
    id_sede = models.ForeignKey('animals.Sede', models.DO_NOTHING, db_column='id_sede')
    fecha_inicio_evento = models.DateTimeField()
    fecha_fin_evento = models.DateTimeField()
    cupo_maximo_evento = models.IntegerField(blank=True, null=True)
    id_voluntarioorganizador = models.ForeignKey('users.Voluntario', models.DO_NOTHING, db_column='id_voluntarioorganizador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Evento'


class Eventoasistente(models.Model):
    pk = models.CompositePrimaryKey('id_evento', 'id_persona')
    id_evento = models.ForeignKey('events.Evento', models.DO_NOTHING, db_column='id_evento')
    id_persona = models.ForeignKey('users.Persona', models.DO_NOTHING, db_column='id_persona')

    class Meta:
        managed = False
        db_table = 'EventoAsistente'


class Eventotipo(models.Model):
    id_eventotipo = models.AutoField(primary_key=True)
    nombre_eventotipo = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'EventoTipo'
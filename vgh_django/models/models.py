# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clase(models.Model):
    clase_id = models.AutoField(primary_key=True)  # The composite primary key (clase_id, nivel_id, grado, seccion_id, profesor_id, departamento_id) found, that is not supported. The first column is selected.
    nivel = models.ForeignKey('Nivel', models.DO_NOTHING)
    grado = models.ForeignKey('Grado', models.DO_NOTHING, db_column='grado')
    seccion = models.ForeignKey('Seccion', models.DO_NOTHING)
    matria = models.CharField(max_length=45)
    profesor = models.ForeignKey('Profesor', models.DO_NOTHING)
    ano = models.TextField()  # This field type is a guess.
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clase'
        unique_together = (('clase_id', 'nivel', 'grado', 'seccion', 'profesor', 'departamento'),)


class Departamento(models.Model):
    departamento_id = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'departamento'


class Estudiante(models.Model):
    estudiante_id = models.AutoField(primary_key=True)  # The composite primary key (estudiante_id, tutoria_id) found, that is not supported. The first column is selected.
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    tutoria = models.ForeignKey('Tutoria', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'estudiante'
        unique_together = (('estudiante_id', 'tutoria'),)


class EstudianteTieneClase(models.Model):
    estudiante_tiene_clase_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING)
    clase = models.ForeignKey(Clase, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'estudiante_tiene_clase'


class Grado(models.Model):
    grado = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'grado'


class Nivel(models.Model):
    nivel_id = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'nivel'


class NotasDeEstudiante(models.Model):
    nota_id = models.AutoField(primary_key=True)  # The composite primary key (nota_id, estudiante_tiene_clase_id) found, that is not supported. The first column is selected.
    bimestre = models.SmallIntegerField()
    nota = models.CharField(max_length=2, blank=True, null=True)
    comentario = models.CharField(max_length=300, blank=True, null=True)
    estudiante_tiene_clase = models.ForeignKey(EstudianteTieneClase, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notas_de_estudiante'
        unique_together = (('nota_id', 'estudiante_tiene_clase'),)


class Profesor(models.Model):
    profesor_id = models.AutoField(primary_key=True)  # The composite primary key (profesor_id, departamento_id) found, that is not supported. The first column is selected.
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    tutor = models.IntegerField()
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profesor'
        unique_together = (('profesor_id', 'departamento'),)
        db_table_comment = '\t'


class Seccion(models.Model):
    seccion_id = models.AutoField(primary_key=True)
    seccion = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'seccion'


class Tutoria(models.Model):
    tutoria_id = models.AutoField(primary_key=True)  # The composite primary key (tutoria_id, nivel_id, grado, seccion_id) found, that is not supported. The first column is selected.
    ano = models.TextField()  # This field type is a guess.
    profesor = models.ForeignKey(Profesor, models.DO_NOTHING)
    nivel = models.ForeignKey(Nivel, models.DO_NOTHING)
    grado = models.ForeignKey(Grado, models.DO_NOTHING, db_column='grado')
    seccion = models.ForeignKey(Seccion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tutoria'
        unique_together = (('tutoria_id', 'nivel', 'grado', 'seccion'),)


class Usario(models.Model):
    usario_id = models.AutoField(primary_key=True)  # The composite primary key (usario_id, profesor_id) found, that is not supported. The first column is selected.
    correo = models.CharField(max_length=45)
    auth_nivel = models.SmallIntegerField()
    auth_id = models.CharField(max_length=45)
    profesor = models.ForeignKey(Profesor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usario'
        unique_together = (('usario_id', 'profesor'),)

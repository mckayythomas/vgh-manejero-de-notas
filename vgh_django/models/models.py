# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    estudiante = models.OneToOneField(Estudiante, models.DO_NOTHING, primary_key=True)  # The composite primary key (estudiante_id, clase_id) found, that is not supported. The first column is selected.
    clase = models.ForeignKey(Clase, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'estudiante_tiene_clase'
        unique_together = (('estudiante', 'clase'),)


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
    clase = models.OneToOneField(Clase, models.DO_NOTHING, primary_key=True)  # The composite primary key (clase_id, estudiante_id) found, that is not supported. The first column is selected.
    estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING)
    ano = models.TextField()  # This field type is a guess.
    bimestre = models.SmallIntegerField()
    nota = models.CharField(max_length=2, blank=True, null=True)
    comentario = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notas_de_estudiante'
        unique_together = (('clase', 'estudiante'),)


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

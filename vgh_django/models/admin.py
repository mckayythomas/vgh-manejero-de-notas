from django.contrib import admin
from models.models import Clase, Departamento, Estudiante, EstudianteTieneClase, Grado, Nivel, NotasDeEstudiante, Profesor, Seccion, Tutoria, Usario

# Register your models here.
admin.site.register(Clase)
admin.site.register(Departamento)
admin.site.register(Estudiante)
admin.site.register(EstudianteTieneClase)
admin.site.register(Grado)
admin.site.register(Nivel)
admin.site.register(NotasDeEstudiante)
admin.site.register(Profesor)
admin.site.register(Seccion)
admin.site.register(Tutoria)
admin.site.register(Usario)

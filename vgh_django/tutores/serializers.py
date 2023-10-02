from rest_framework import serializers
from models.models import Tutoria, Estudiante, NotasDeEstudiante, Clase, EstudianteTieneClase


# Serializer to view estudiantes in tutoria
class TutoriaEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
# create serializer for estudiantes

# Serializer to view students grades based on student id
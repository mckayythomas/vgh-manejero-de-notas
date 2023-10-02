from rest_framework import serializers
from models.models import Profesor, Tutoria, EstudianteTieneClase, Nivel, NotasDeEstudiante, Seccion, Estudiante, Clase

class NivelSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Nivel
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Seccion
        fields = '__all__'

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase,
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

# Serializer to view tutoria in Nivel
class TutoriaDeNivelSerializer(serializers.ModelSerializer):
    profesor = ProfesorSerializer()
    class Meta:
        model = Tutoria
        fields = '__all__'

    def to_representation(self, instance):
        # Extract profesor data
        profesor_data = {
            "profesor_id": instance.profesor.profesor_id,
            "nombres": instance.profesor.nombres,
            "apellidos": instance.profesor.apellidos,
            "departamento": instance.profesor.departamento.departamento
        }

        representation = {
            "tutoria_id": instance.tutoria_id,
            "ano": instance.ano,
            "nivel": instance.nivel.nivel,
            "grado": instance.grado.grado,
            "seccion": instance.seccion.seccion,
            "profesor": profesor_data
        }

        return representation

    # {
    #     "tutoria_id": 15,
    #     "profesor": {
    #         "profesor_id": 23,
    #         "nombres": "Camilo Andres",
    #         "apellidos": "Ramirez Castillo",
    #         "tutor": 1,
    #         "departamento": 1
    #     },
    #     "ano": "2023",
    #     "nivel": 1,
    #     "grado": 1,
    #     "seccion": 1
    # },    

# Serializer to view estudiantes in tutoria
class TutoriaEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


# serializer for clase
class ClaseSerializer(serializers.ModelSerializer):
    class Meta():
        model = Clase
        fields = '__all__'

# serializer for estudiante_tiene_clase
class EstudianteTieneClaseSerializer(serializers.ModelSerializer):
    estudiante = TutoriaEstudianteSerializer()
    clase = ClaseSerializer()
    class Meta():
        model = EstudianteTieneClase
        fields = '__all__'

# serializer for notas 
class NotasDeEstudianteSerializer(serializers.ModelSerializer):
    estudiante_tiene_clase = EstudianteTieneClaseSerializer()
    class Meta():
        model = NotasDeEstudiante
        fields = '__all__'
    
    def to_representation(self, instance):
        # representation = super().to_representation(instance)
        
        # Extract relevant fields from the representation
        nota_data = {
            "nota_id": instance.nota_id,
            "bimestre": instance.bimestre,
            "nota": instance.nota,
            "comentario": instance.comentario
        }

        clase_data = {
            "clase_id": instance.estudiante_tiene_clase.clase.clase_id,
            "nivel": instance.estudiante_tiene_clase.clase.nivel.nivel,
            "grado": instance.estudiante_tiene_clase.clase.grado.grado,
            "seccion": instance.estudiante_tiene_clase.clase.seccion.seccion,
            "matria": instance.estudiante_tiene_clase.clase.matria,
            "ano": instance.estudiante_tiene_clase.clase.ano,
            "nota": nota_data,

        }

        estudiante_data = {
            "estudiante": instance.estudiante_tiene_clase.estudiante.estudiante_id,
            "nombres": instance.estudiante_tiene_clase.estudiante.nombres,
            "apellidos": instance.estudiante_tiene_clase.estudiante.apellidos,
            "clase": clase_data
        }

        representation = {
            "estudiante_tiene_clase_id": instance.estudiante_tiene_clase.estudiante_tiene_clase_id,  # Corrected attribute name here
            "estudiante": estudiante_data,
        }

        return representation
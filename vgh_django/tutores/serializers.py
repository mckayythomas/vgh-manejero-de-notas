from rest_framework import serializers
from models.models import Tutoria, Estudiante, NotasDeEstudiante, Clase, EstudianteTieneClase


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
    # {
    #     "nota_id": 586,
    #     "estudiante_tiene_clase": {
    #         "estudiante_tiene_clase_id": 766,
    #         "estudiante": {
    #             "estudiante_id": 46,
    #             "nombres": "Fernando",
    #             "apellidos": "Hernandez Molina",
    #             "tutoria": 4
    #         },
    #         "clase": {
    #             "clase_id": 4,
    #             "matria": "CIENCIA Y TECNOLOGÍA",
    #             "ano": "2023",
    #             "nivel": 2,
    #             "grado": 2,
    #             "seccion": 2,
    #             "profesor": 6,
    #             "departamento": 2
    #         }
    #     },
    #     "bimestre": 1,
    #     "nota": null,
    #     "comentario": null
    # },
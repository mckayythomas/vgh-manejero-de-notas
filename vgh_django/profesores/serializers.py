from rest_framework import serializers
from models.models import Clase, Estudiante, NotasDeEstudiante, Nivel, Seccion, EstudianteTieneClase

# GET request serializers
class NivelSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Nivel
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Seccion
        fields = '__all__'
class ClaseDetallesSerializer(serializers.ModelSerializer):
    nivel = NivelSerializer(read_only=True)
    seccion = SeccionSerializer(read_only=True)

    class Meta:
        model = Clase
        fields = '__all__'

    def get_clase_de_profesor(self, profesor_id):
        return Clase.objects.filter(profesor_id=profesor_id)
    
    def to_representation(self, instance):
        representation = super(ClaseDetallesSerializer, self).to_representation(instance)

        # Extract relevant fields from the representation
        clase_id = representation['clase_id']
        matria = representation['matria']
        ano = representation['ano']
        grado = representation['grado']
        profesor = representation['profesor']
        departamento = representation['departamento']
        seccion = representation['seccion']['seccion'] 
        nivel = representation['nivel']['nivel']

        # Create the formatted representation
        formatted_data = {
            'clase_id': clase_id,
            'matria': matria,
            'ano': ano,
            'nivel': nivel,
            'grado': grado,
            'seccion': seccion,
            'profesor_id': profesor,
            'departamento': departamento,

        }

        return formatted_data
    
class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class EstudianteTieneClaseSerializer(serializers.ModelSerializer):
    estudiante = EstudianteSerializer()

    class Meta:
        model = EstudianteTieneClase
        fields = '__all__'

from rest_framework import serializers

class NotasDeEstudianteSerializer(serializers.ModelSerializer):
    estudiante_tiene_clase = EstudianteTieneClaseSerializer()

    class Meta:
        model = NotasDeEstudiante
        fields = '__all__'

    def to_representation(self, instance):
        # Serialize the nota nested data
        nota_data = {
            "nota_id": instance.nota_id,
            "bimestre": instance.bimestre,
            "nota": instance.nota,
            "comentario": instance.comentario
        }

        # Serialize the student object
        estudiante_data = {
            "estudiante_id": instance.estudiante_tiene_clase.estudiante.estudiante_id,
            "nombres": instance.estudiante_tiene_clase.estudiante.nombres,
            "apellidos": instance.estudiante_tiene_clase.estudiante.apellidos,
            "nota": nota_data         
        }

        etc_data = {
            "estudiante_tiene_clase_id": instance.estudiante_tiene_clase.estudiante_tiene_clase_id,
            "clase_id": instance.estudiante_tiene_clase.clase.clase_id
        }

        # Construct the final representation
        representation = {
            "estudiante": estudiante_data,
            "estudiante_tiene_clase": etc_data
        }

        return representation


# PUT request serializer
class NotasDeEstudianteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotasDeEstudiante
        fields = ['nota', 'comentario']

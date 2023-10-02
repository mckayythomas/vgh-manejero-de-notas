from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from models.models import Estudiante, NotasDeEstudiante
from tutores.serializers import TutoriaEstudianteSerializer, NotasDeEstudianteSerializer

# Create your views here.
# Get tutoria class
class TutoriaDashboard(viewsets.ViewSet):
    @action(detail=False, methods=['GET'], url_path='tutoria/(?P<tutoria_id>/d+)/estudiantes')
    def tutoriaEstudiantes(self, request, tutoria_id):
        try:
            # Check if the profesor exists
            if not Estudiante.objects.filter(tutoria_id=tutoria_id).exists():
                raise NotFound('Tutoria with the given ID doesn\'t exist.')
            
            estudiantes = Estudiante.objects.filter(tutoria_id=tutoria_id)
            # Check if there are classes for profesor
            if not estudiantes:
                raise NotFound('No classes found for the given profesor.')
            
            serializer = TutoriaEstudianteSerializer(estudiantes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)        
        except NotFound as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)

    # Get students grades
    def getNotas(self, request, estudiante_id):
        try:
            # Check if nota exists
            if not Estudiante.objects.filter(estudiante_id=estudiante_id).exists():
                raise NotFound('Estudiante with the given ID doen\'t exist.')
            
            notas = NotasDeEstudiante.objects.filter(estudiante_tiene_clase__estudiante_id=estudiante_id)
            # Check that there are notas for the student
            if not notas:
                raise NotFound('No notas for the estudiante found.')
            
            serializer = NotasDeEstudianteSerializer(notas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


        except NotFound as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)


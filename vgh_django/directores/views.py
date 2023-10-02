from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.exceptions import NotFound
from models.models import Nivel, Estudiante, NotasDeEstudiante, Tutoria
from directores.serializers import TutoriaDeNivelSerializer, TutoriaEstudianteSerializer, NotasDeEstudianteSerializer

# Create your views here.
class DirectorDashboard(viewsets.ViewSet):
    def nivelTutoria(self, request, nivel_id):
        try:
            # Check if nivel Id is valid
            if not Nivel.objects.filter(nivel_id=nivel_id).exists():
                raise NotFound('Nivel with the given ID doesn\'t exist.')
            tutorias = Tutoria.objects.filter(nivel_id=nivel_id)
            # Checkthat there are clases to return
            if not tutorias:
                raise NotFound('No tutorias for the nivel found.')
            serializer = TutoriaDeNivelSerializer(tutorias, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)
            
    def estudiantesDeTutoria(self, request, tutoria_id):
        try:
            # check if clase_id is valid
            if not Tutoria.objects.filter(tutoria_id=tutoria_id).exists():
                raise NotFound('Clase with the given ID doesn\'t exist.')
            
            estudiantes = Estudiante.objects.filter(tutoria_id=tutoria_id)
            # check that estudiantes have data to return
            if not estudiantes:
                raise NotFound('No estudiantes for the tutoria found.')
            serializer = TutoriaEstudianteSerializer(estudiantes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({'messege': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def notasDeEstudiante(self, request, estudiante_id):
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
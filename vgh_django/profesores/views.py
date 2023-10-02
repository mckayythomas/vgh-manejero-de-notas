from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from models.models import Clase, NotasDeEstudiante
from profesores.serializers import ClaseDetallesSerializer, NotasDeEstudianteSerializer

class ProfesorDashboard(viewsets.ViewSet):
    @action(detail=False, methods=['GET'], url_path='profesores/(?P<profesor_id>\d+)/clases')
    def clases(self, request, profesor_id):
        try:
            # Check if the profesor exists
            if not Clase.objects.filter(profesor_id=profesor_id).exists():
                raise NotFound('Professor with the given ID doesn\'t exist.')
            
            professor_classes = Clase.objects.filter(profesor_id=profesor_id)

            # Check if there are classes for profesor
            if not professor_classes:
                raise NotFound('No classes found for the given profesor.')
            
            serializer = ClaseDetallesSerializer(professor_classes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)        
        except NotFound as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def estudiantes(self, request, clase_id):
        try:
            # Check is a class id exists
            if not Clase.objects.filter(clase_id=clase_id).exists():
                raise NotFound('Clase with given ID doesn\'t exist')
            print('works')
            notas = NotasDeEstudiante.objects.filter(estudiante_tiene_clase__clase_id=clase_id)
            print('works2')
            # check if there is estudiantes in a class
            if not notas:
                raise NotFound('No estudiantes found for the given clase.')
            
            serializer = NotasDeEstudianteSerializer(notas, many=True)
            print('works3')
            return Response(serializer.data, status=status.HTTP_200_OK)

        except NotFound as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)

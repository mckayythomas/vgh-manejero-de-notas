from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ValidationError
from models.models import Clase, NotasDeEstudiante
from profesores.serializers import ClaseDetallesSerializer, NotasDeEstudianteSerializer, NotasDeEstudianteUpdateSerializer

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
            notas = NotasDeEstudiante.objects.filter(estudiante_tiene_clase__clase_id=clase_id)
            # check if there is estudiantes in a class
            if not notas:
                raise NotFound('No estudiantes found for the given clase.')
            
            serializer = NotasDeEstudianteSerializer(notas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except NotFound as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['PUT'], url_path='nota/(?P<nota_id>\d+)/update')
    def updateNotas(self, request, nota_id):
        try:    
            nota_instance = NotasDeEstudiante.objects.get(nota_id=nota_id)
    
            if not nota_instance:
                raise NotFound('Nota or Estudiante Tiene Nota with the given ID doesn\'t exist.')
    
            # Check if fields are valid
            new_nota = request.data.get('nota', nota_instance.nota)
            new_comentario = request.data.get('comentario', nota_instance.comentario)
    
            if not new_nota or not new_comentario:
                raise ValidationError('Missing either the nota or comentario fields in request body.')
    
            # Update nota and comentario fields
            nota_instance.nota = new_nota
            nota_instance.comentario = new_comentario
            serializer = NotasDeEstudianteUpdateSerializer(nota_instance)
            
            try:
                nota_instance.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'message': 'Something went wrong. Couldn\'t update the nota'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except NotasDeEstudiante.DoesNotExist:
            return Response({'message': 'Nota or Estudiante Tiene Nota with the given ID doesn\'t exist.'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from models.models import Estudiante
from tutores.serializers import TutoriaEstudianteSerializer

# Create your views here.
# Get tutoria class
class TutoriaDashboard(APIView):
    @action(detail=False, methods=['GET'], url_path='tutoria/(?P<tutoria_id>/d+)/estudiantes')
    def get(self, request, tutoria_id):
        try:
            # Check if the profesor exists
            if not Estudiante.objects.filter(tutoria_id=tutoria_id).exists():
                raise NotFound('Tutoria with the given ID doesn\'t exist.')
            
            estudiantes = Estudiante.objects.filter(tutoria_id=tutoria_id)
            print(estudiantes)
            # Check if there are classes for profesor
            if not estudiantes:
                raise NotFound('No classes found for the given profesor.')
            
            serializer = TutoriaEstudianteSerializer(estudiantes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)        
        except NotFound as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)

# Get students grades
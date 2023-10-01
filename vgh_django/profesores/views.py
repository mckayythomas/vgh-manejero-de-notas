from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from models.models import Clase
from profesores.serializers import ClaseSerializer

class ProfesorDashboard(viewsets.ViewSet):
    @action(detail=False, methods=['GET'], url_path='profesores/(?P<profesor_id>\d+)/clases')
    def clases(self, request, profesor_id):
        professor_classes = Clase.objects.filter(profesor_id=profesor_id)
        serializer = ClaseSerializer(professor_classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        
    # def estudiantes(self, request):



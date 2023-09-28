from django.http import JsonResponse
from models.models import Seccion
from models.serializers import TestSerializer

# Create your views here.
def get_seccion(request):
    secciones = Seccion.objects.all()
    serializer = TestSerializer(secciones, many=True)
    return JsonResponse({'seccionses' : serializer.data}, safe=False)
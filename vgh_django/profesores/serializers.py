from rest_framework import serializers
from models.models import Clase, Nivel, Seccion

class ClaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clase
        fields = '__all__'

    def get_clase_de_profesor(self, profesor_id):
        return Clase.objects.filter(profesor_id=profesor_id)
from rest_framework import serializers
from models.models import Seccion

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = ['seccion_id', 'seccion']

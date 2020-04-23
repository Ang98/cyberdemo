from rest_framework import serializers
from ..models.Conferencia import Conferencia

class ConferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencia
        fields = '__all__'

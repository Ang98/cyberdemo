
from rest_framework import serializers
from ..models.ExamenPregunta import ExamenPregunta


class ExamenPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenPregunta
        fields = '__all__'

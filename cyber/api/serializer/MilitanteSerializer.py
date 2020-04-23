
from rest_framework import serializers
from ..models.Militante import Militante


class MilitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Militante
        fields = '__all__'

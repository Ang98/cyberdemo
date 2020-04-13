

from rest_framework import serializers
from ..models import MilitanteExamen


class MilitanteExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitanteExamen
        fields = '__all__'

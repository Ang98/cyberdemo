
from rest_framework import serializers
from ..models import Externo


class ExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Externo
        fields = '__all__'

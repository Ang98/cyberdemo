
from rest_framework import serializers
from ..models.Alternativa import Alternativa


class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = '__all__'

""" Partido Politico """
from rest_framework import serializers

from models import PartidoPolitico

class PartidoPoliticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidoPolitico
        fields = '__all__'

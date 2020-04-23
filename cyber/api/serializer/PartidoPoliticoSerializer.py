""" Partido Politico """
from rest_framework import serializers
from ..models.PartidoPolitico import PartidoPolitico


class PartidoPoliticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidoPolitico
        fields = '__all__'

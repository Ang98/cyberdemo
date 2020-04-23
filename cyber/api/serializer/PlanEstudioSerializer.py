from rest_framework import serializers
from ..models.PlanEstudio import PlanEstudio



class PlanEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEstudio
        fields = '__all__'

from rest_framework import serializers
from ..models.SecretariaPP import SecretariaPP



class SecretariaPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretariaPP
        fields = '__all__'

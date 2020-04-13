from rest_framework import serializers
from ..models import SecretariaPP



class SecretariaPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretariaPP
        fields = '__all__'

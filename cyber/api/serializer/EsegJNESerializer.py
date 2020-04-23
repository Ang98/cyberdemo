from rest_framework import serializers
from ..models.EsegJNE import EsegJNE


class EsegJNESerializer(serializers.ModelSerializer):
    class Meta:
        model = EsegJNE
        fields = '__all__'

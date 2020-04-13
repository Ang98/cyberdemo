from rest_framework import serializers
from ..models import EsegJNE


class EsegJNESerializer(serializers.ModelSerializer):
    class Meta:
        model = EsegJNE
        fields = '__all__'

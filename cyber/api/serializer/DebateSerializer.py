from rest_framework import serializers
from ..models.Debate import Debate



class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = '__all__'

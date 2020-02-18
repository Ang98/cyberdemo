from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PartidoPoliticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidoPolitico
        fields = '__all__'

class EsegJNESerializer(serializers.ModelSerializer):
    class Meta:
        model = EsegJNE
        fields = '__all__'


class PlanEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEstudio
        fields = '__all__'


class SecretariaPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretariaPP
        fields = '__all__'

class MilitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Militante
        fields = '__all__'

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = '__all__'

class MilitanteExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitanteExamen
        fields = '__all__'


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

class ExamenPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenPregunta
        fields = '__all__'

class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class ConferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencia
        fields = '__all__'


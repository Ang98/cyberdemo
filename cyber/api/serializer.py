from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import *


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
        fields = ['id','nombre','estado','fecha_registro','usuario_registro','fecha_modificacion','usuario_modificacion',]

class EsejJNESerializer(serializers.ModelSerializer):
    class Meta:
        model = EsegJNE
        fields=['id','estado','dni_responsable','apellidos','nombres','sugerencia','observacion',]


class PlanEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEstudio
        fields = ['id','id_seg','nombre','estado',]


class SecretariaPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretariaPP
        fields = ['id','id_partido','nombre','descripcion','responsable',]

class MilitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Militante
        fields = ['id','id_militante','id_plan','id_partido','dni','apellidos','nombres','perfil']

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = ['id','tipo','responsable',]

class MilitanteExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitanteExamen
        fields = ['id','id_militante','id_examen','nota',]


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields=['id','contenido','fecha_registro','usuario_registro','fecha_modificacion','usuario_modificacion',]

class ExamenPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenPregunta
        fields=['id','id_examen','id_pregunta','fecha_registro','usuario_registro','fecha_modificacion','usuario_modificacion',]

class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields=['id','id_militante','tema','estado','moderador','fecha_registro','usuario_registro','fecha_modificacion','usuario_modificacion',]

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields=['id','id_militante','usuario','contra','fecha_registro','usuario_registro','fecha_modificacion','usuario_modificacion',]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields=['id','id_pan','nombre_curso','sumilla','docente','fecha_registro','usuario_registro','fecha_modificacion','usuario_modificacion',]

class ConferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencia
        fields=['id','id_plan','tema','apellidos_conferencista','nombres_conferenciasta','tipo','fecha_registro','usuario_registro','fecha_modificacion','usuario_modificacion',]


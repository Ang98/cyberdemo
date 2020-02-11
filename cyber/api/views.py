from django.shortcuts import render

#CYBER
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import *
from .models import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PartidoPoliticoViewset(viewsets.ModelViewSet):
    queryset = PartidoPolitico.objects.all()
    serializer_class = PartidoPoliticoSerializer

class EsegJNEViewSet(viewsets.ModelViewSet):
    queryset = EsegJNE.objects.all()
    serializer_class = EsegJNESerializer

class PlanEstudioViewSet(viewsets.ModelViewSet):
    queryset = PlanEstudio.objects.all()
    serializer_class = PlanEstudioSerializer


class SecretariaPPViewSet(viewsets.ModelViewSet):
    queryset = SecretariaPP.objects.all()
    serializer_class = SecretariaPPSerializer

class MilitanteViewSet(viewsets.ModelViewSet):
    queryset = Militante.objects.all()
    serializer_class = MilitanteSerializer

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class MilitanteExamenViewSet(viewsets.ModelViewSet):
    queryset = MilitanteExamen.objects.all()
    serializer_class = MilitanteExamenSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class ExamenPreguntaViewSet(viewsets.ModelViewSet):
    queryset = ExamenPregunta.objects.all()
    serializer_class = ExamenPreguntaSerializer

class DebateViewSet(viewsets.ModelViewSet):
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ConferenciaViewSet(viewsets.ModelViewSet):
    queryset = Conferencia.objects.all()
    serializer_class = ConferenciaSerializer


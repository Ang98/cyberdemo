
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from .serializer import *
from ..models import *


class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

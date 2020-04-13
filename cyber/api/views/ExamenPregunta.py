
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from .serializer import *
from ..models import *


class ExamenPreguntaViewSet(viewsets.ModelViewSet):
    queryset = ExamenPregunta.objects.all()
    serializer_class = ExamenPreguntaSerializer

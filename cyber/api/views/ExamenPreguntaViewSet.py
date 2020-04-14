
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.ExamenPreguntaSerializer import *
from ..models.ExamenPregunta import *


class ExamenPreguntaViewSet(viewsets.ModelViewSet):
    queryset = ExamenPregunta.objects.all()
    serializer_class = ExamenPreguntaSerializer

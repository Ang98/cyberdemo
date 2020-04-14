from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.ExamenSerializer import *
from ..models.Examen import *


class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer


from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.CursoSerializer import *
from ..models.Curso import *


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

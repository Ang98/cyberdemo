from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.PartidoPoliticoSerializer import PartidoPoliticoSerializer
from ..models.PartidoPolitico import PartidoPolitico 


class PartidoPoliticoViewSet(viewsets.ModelViewSet):
    queryset = PartidoPolitico.objects.all()
    serializer_class = PartidoPoliticoSerializer

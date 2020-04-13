from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from .serializer import *
from ..models import *


class PartidoPoliticoViewset(viewsets.ModelViewSet):
    queryset = PartidoPolitico.objects.all()
    serializer_class = PartidoPoliticoSerializer


from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from .serializer import *
from ..models import *


class MilitanteExamenViewSet(viewsets.ModelViewSet):
    queryset = MilitanteExamen.objects.all()
    serializer_class = MilitanteExamenSerializer

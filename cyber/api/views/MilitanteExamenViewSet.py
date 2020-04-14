
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.MilitanteExamenSerializer import *
from ..models.MilitanteExamen import *


class MilitanteExamenViewSet(viewsets.ModelViewSet):
    queryset = MilitanteExamen.objects.all()
    serializer_class = MilitanteExamenSerializer

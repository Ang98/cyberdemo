
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.MilitanteSerializer import *
from ..models.Militante import *


class MilitanteViewSet(viewsets.ModelViewSet):
    queryset = Militante.objects.all()
    serializer_class = MilitanteSerializer

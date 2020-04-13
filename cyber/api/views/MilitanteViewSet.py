
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from .serializer import *
from ..models import *


class MilitanteViewSet(viewsets.ModelViewSet):
    queryset = Militante.objects.all()
    serializer_class = MilitanteSerializer

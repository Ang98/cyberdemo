
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from .serializer import *
from ..models import *


class ExternoViewSet(viewsets.ModelViewSet):
    queryset = Externo.objects.all()
    serializer_class = ExternoSerializer

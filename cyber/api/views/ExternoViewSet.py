
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.ExternoSerializer import *
from ..models.Externo import *


class ExternoViewSet(viewsets.ModelViewSet):
    queryset = Externo.objects.all()
    serializer_class = ExternoSerializer

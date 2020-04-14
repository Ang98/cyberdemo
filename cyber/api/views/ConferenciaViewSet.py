from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.ConferenciaSerializer import *
from ..models.Conferencia import *


class ConferenciaViewSet(viewsets.ModelViewSet):
    queryset = Conferencia.objects.all()
    serializer_class = ConferenciaSerializer

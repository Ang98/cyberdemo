from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.AlternativaSerializer import *
from ..models.Alternativa import *


class AlternativaViewSet(viewsets.ModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer

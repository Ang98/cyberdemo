from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.PlanEstudioSerializer import *
from ..models.PlanEstudio import *


class PlanEstudioViewSet(viewsets.ModelViewSet):
    queryset = PlanEstudio.objects.all()
    serializer_class = PlanEstudioSerializer

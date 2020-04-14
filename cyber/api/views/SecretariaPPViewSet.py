
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.SecretariaPPSerializer import *
from ..models.SecretariaPP import *


class SecretariaPPViewSet(viewsets.ModelViewSet):
    queryset = SecretariaPP.objects.all()
    serializer_class = SecretariaPPSerializer

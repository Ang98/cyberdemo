
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from .serializer import *
from ..models import *


class SecretariaPPViewSet(viewsets.ModelViewSet):
    queryset = SecretariaPP.objects.all()
    serializer_class = SecretariaPPSerializer

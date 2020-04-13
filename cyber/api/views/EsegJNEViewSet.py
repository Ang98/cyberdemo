from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from .serializer import *
from ..models import *


class EsegJNEViewSet(viewsets.ModelViewSet):
    queryset = EsegJNE.objects.all()
    serializer_class = EsegJNESerializer

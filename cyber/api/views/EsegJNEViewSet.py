from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.EsegJNESerializer import *
from ..models.EsegJNE import *


class EsegJNEViewSet(viewsets.ModelViewSet):
    queryset = EsegJNE.objects.all()
    serializer_class = EsegJNESerializer

from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from .serializer import *
from ..models import *


class DebateViewSet(viewsets.ModelViewSet):
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer

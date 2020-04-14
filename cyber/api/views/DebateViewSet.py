from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.DebateSerializer import *
from ..models.Debate import *


class DebateViewSet(viewsets.ModelViewSet):
    queryset = Debate.objects.all()
    serializer_class = DebateSerializer

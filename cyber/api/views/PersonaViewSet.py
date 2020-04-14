from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.PersonaSerializer import *
from ..models.Persona import *


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.ExamenPreguntaSerializer import *
from ..models.ExamenPregunta import *


class ExamenPreguntaViewSet(viewsets.ModelViewSet):
    
    serializer_class = ExamenPreguntaSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = ExamenPregunta.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']
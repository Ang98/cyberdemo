from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.ExamenSerializer import *
from ..models.Examen import *


class ExamenViewSet(viewsets.ModelViewSet):

    serializer_class = ExamenSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Examen.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']
        
    
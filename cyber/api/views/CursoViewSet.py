
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.CursoSerializer import *
from ..models.Curso import *


class CursoViewSet(viewsets.ModelViewSet):
    
    serializer_class = CursoSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Curso.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']
        
    

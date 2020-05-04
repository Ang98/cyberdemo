from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.PartidoPoliticoSerializer import PartidoPoliticoSerializer
from ..models.PartidoPolitico import PartidoPolitico 


class PartidoPoliticoViewSet(viewsets.ModelViewSet):
    
    serializer_class = PartidoPoliticoSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = PartidoPolitico.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']

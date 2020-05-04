from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.ConferenciaSerializer import *
from ..models.Conferencia import *


class ConferenciaViewSet(viewsets.ModelViewSet):
    
    serializer_class = ConferenciaSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Conferencia.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']
        
    

from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.ExternoSerializer import *
from ..models.Externo import *


class ExternoViewSet(viewsets.ModelViewSet):
    
    serializer_class = ExternoSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Externo.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']

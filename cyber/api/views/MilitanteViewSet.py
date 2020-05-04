
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.MilitanteSerializer import *
from ..models.Militante import *


class MilitanteViewSet(viewsets.ModelViewSet):
    
    serializer_class = MilitanteSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Militante.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']
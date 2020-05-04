
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.MilitanteExamenSerializer import *
from ..models.MilitanteExamen import *


class MilitanteExamenViewSet(viewsets.ModelViewSet):
    queryset = MilitanteExamen.objects.all()
    serializer_class = MilitanteExamenSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = MilitanteExamen.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']

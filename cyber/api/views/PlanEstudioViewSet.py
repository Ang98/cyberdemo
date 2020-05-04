from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.PlanEstudioSerializer import *
from ..models.PlanEstudio import *


class PlanEstudioViewSet(viewsets.ModelViewSet):
    
    serializer_class = PlanEstudioSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = PlanEstudio.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']


from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.SecretariaPPSerializer import *
from ..models.SecretariaPP import *


class SecretariaPPViewSet(viewsets.ModelViewSet):
    
    serializer_class = SecretariaPPSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = SecretariaPP.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.EsegJNESerializer import *
from ..models.EsegJNE import *


class EsegJNEViewSet(viewsets.ModelViewSet):
    
    serializer_class = EsegJNESerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = EsegJNE.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']

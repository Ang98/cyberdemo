from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializer.AlternativaSerializer import *
from ..models.Alternativa import *


class AlternativaViewSet(viewsets.ModelViewSet):
    
    serializer_class = AlternativaSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Alternativa.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']
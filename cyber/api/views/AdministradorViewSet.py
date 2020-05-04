
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.AdministradoSerializer import AdministradorSerializer
from ..models.Administrador import Administrador


class AdministradorViewSet(viewsets.ModelViewSet):

    serializer_class = AdministradorSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Administrador.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']

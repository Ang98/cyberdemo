
from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from ..serializer.AdministradoSerializer import AdministradorSerializer
from ..models.Administrador import Administrador


class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

from django.shortcuts import render

# CYBER
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializer.DebateSerializer import *
from ..models.Debate import *


class DebateViewSet(viewsets.ModelViewSet):
    
    serializer_class = DebateSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Debate.objects.all()
        usuario = self.request.user
        if usuario.is_administrador:
            return queryset
        return ['Usuario no es administrador']
        
from django.shortcuts import render

#CYBER
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
""" Usuarios URL"""

from django.urls import path 

from usuarios.views import *

urlpatterns = [
    path('usuarios/login/',UsuarioLoginAPIView.as_view(), name='login'),
    path('usuarios/signup/',UsuarioSignupAPIView.as_view(), name='signup')
]

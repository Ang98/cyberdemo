"""
Administrador
"""
from django.db import models


class Administrador(models.Model):
    """ atributos propios de adminsitrador"""
    usuario=  models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE)
    cargo = models.CharField(max_length=20, blank=True, default='')

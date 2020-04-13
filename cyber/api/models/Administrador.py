"""
Administrador
"""
from django.db import models
from Persona import Persona


class Administrador(Persona):
    """ atributos propios de adminsitrador"""
    cargo = models.CharField(max_length=20, blank=True, default='')

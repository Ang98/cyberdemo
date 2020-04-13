"""
Externo
"""

from django.db import models

from Persona import Persona


class Externo(Persona):

    """ atributos propios de externo"""
    descripcion = models.CharField(max_length=400, blank=True, default='')

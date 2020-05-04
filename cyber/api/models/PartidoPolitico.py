"""
Partido Politico
"""
from django.db import models

from utils.models import Auditoria

class PartidoPolitico(Auditoria,models.Model):
    """ atributos propios de partido politico"""
    nombre = models.CharField(max_length=45, blank=True, default='')
    estado = models.CharField(max_length=45, blank=True, default='')


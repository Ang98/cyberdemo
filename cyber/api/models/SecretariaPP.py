"""
Secreatria Partido Politico
"""

from django.db import models
from .PartidoPolitico import PartidoPolitico

from utils.models import Auditoria

class SecretariaPP(Auditoria,models.Model):
    """ atributos foraneos"""
    id_partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)

    """atributos propios de secretaria partido politico"""
    nombre = models.CharField(max_length=45, blank=True, default='')
    descripcion = models.CharField(max_length=200, blank=True, default='')
    responsable = models.CharField(max_length=45, blank=True, default='')

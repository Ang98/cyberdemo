"""
Debate
"""
from django.db import models
from .Militante import Militante

from utils.models import Auditoria

class Debate(Auditoria,models.Model):
    """atributos foraneos"""
    id_militante = models.ForeignKey(Militante, on_delete=models.CASCADE)

    """atributos propios de debate"""
    tema = models.CharField(max_length=45, blank=True, default='')
    estado = models.CharField(max_length=45, blank=True, default='')
    moderador = models.CharField(max_length=45, blank=True, default='')


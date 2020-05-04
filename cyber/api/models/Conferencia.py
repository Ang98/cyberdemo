"""
Conferencia
"""

from django.db import models
from .PlanEstudio import PlanEstudio

from utils.models import Auditoria

class Conferencia(Auditoria,models.Model):

    """atributos foraneos"""
    id_plan = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)

    """atributos propios de conferencia"""
    tema = models.CharField(max_length=45, blank=True, default='')
    apellidos_conferencista = models.CharField(
        max_length=100, blank=True, default='')
    nombres_conferecista = models.CharField(
        max_length=100, blank=True, default='')
    tipo = models.CharField(max_length=45, blank=True, default='')


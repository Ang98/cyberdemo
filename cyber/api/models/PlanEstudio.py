"""
Plan Estudio
"""

from django.db import models
from .EsegJNE import EsegJNE

from utils.models import Auditoria

class PlanEstudio(Auditoria,models.Model):
    """ atributos foraneos"""
    id_seg = models.ForeignKey(EsegJNE, on_delete=models.CASCADE)

    """atributos propios de plan de estudio"""
    nombre = models.CharField(max_length=100, blank=True, default='')
    estado = models.CharField(max_length=45, blank=True, default='')

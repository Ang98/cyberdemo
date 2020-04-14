"""
Plan Estudio
"""

from django.db import models
from .EsegJNE import EsegJNE


class PlanEstudio(models.Model):
    """ atributos foraneos"""
    id_seg = models.ForeignKey(EsegJNE, on_delete=models.CASCADE)

    """atributos propios de plan de estudio"""
    nombre = models.CharField(max_length=100, blank=True, default='')
    estado = models.CharField(max_length=45, blank=True, default='')

    """atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

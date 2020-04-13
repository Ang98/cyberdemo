"""
Examen
"""
from django.db import models


class Examen(models.Model):

    """atributos propios de examen"""
    tipo = models.CharField(max_length=45, blank=True, default='')
    responsable = models.CharField(max_length=45, blank=True, default='')

    """atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

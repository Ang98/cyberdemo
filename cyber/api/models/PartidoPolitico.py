"""
Partido Politico
"""
from django.db import models


class PartidoPolitico(models.Model):
    """ atributos propios de partido politico"""
    nombre = models.CharField(max_length=45, blank=True, default='')
    estado = models.CharField(max_length=45, blank=True, default='')

    """atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

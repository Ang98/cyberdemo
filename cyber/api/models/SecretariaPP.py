"""
Secreatria Partido Politico
"""

from django.db import models
from PartidoPolitico import PartidoPolitico


class SecretariaPP(models.Model):
    """ atributos foraneos"""
    id_partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)

    """atributos propios de secretaria partido politico"""
    nombre = models.CharField(max_length=45, blank=True, default='')
    descripcion = models.CharField(max_length=200, blank=True, default='')
    responsable = models.CharField(max_length=45, blank=True, default='')

    """ atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

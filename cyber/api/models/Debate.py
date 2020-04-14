"""
Debate
"""
from django.db import models
from .Militante import Militante


class Debate(models.Model):
    """atributos foraneos"""
    id_militante = models.ForeignKey(Militante, on_delete=models.CASCADE)

    """atributos propios de debate"""
    tema = models.CharField(max_length=45, blank=True, default='')
    estado = models.CharField(max_length=45, blank=True, default='')
    moderador = models.CharField(max_length=45, blank=True, default='')

    """atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

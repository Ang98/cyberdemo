"""
Pregunta
"""
from django.db import models


class Pregunta(models.Model):

    """atributos propios de pregunta"""
    contenido = models.CharField(max_length=600, blank=True, default='')
    puntaje = models.IntegerField()

    """ atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

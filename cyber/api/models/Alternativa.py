"""
Alternativa
"""
from django.db import models
from .Examen import Examen


class Alternativa(models.Model):

    """atributos foraneos"""
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)

    """atributos propios de alternativa"""

    contenido = models.CharField(max_length=45, blank=True, default='')
    respuesta = models.BooleanField(default=False)

    """ atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

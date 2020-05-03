"""
Alternativa
"""
from django.db import models
from .Examen import Examen

from utils.models import Auditoria

class Alternativa(Auditoria ,models.Model):

    """atributos foraneos"""
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)

    """atributos propios de alternativa"""

    contenido = models.CharField(max_length=45, blank=True, default='')
    respuesta = models.BooleanField(default=False)



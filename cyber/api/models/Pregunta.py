"""
Pregunta
"""
from django.db import models

from utils.models import Auditoria

class Pregunta(Auditoria,models.Model):

    """atributos propios de pregunta"""
    contenido = models.CharField(max_length=600, blank=True, default='')
    puntaje = models.IntegerField()

"""
Examen Pregunta
"""
from django.db import models
from .Examen import Examen
from .Pregunta import Pregunta

from utils.models import Auditoria

class ExamenPregunta(Auditoria,models.Model):

    """ atributos foraneos"""
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)


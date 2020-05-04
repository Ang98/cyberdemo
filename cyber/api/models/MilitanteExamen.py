"""
Militante Examen
"""
from django.db import models
from .Militante import Militante
from .Examen import Examen

from utils.models import Auditoria

class MilitanteExamen(Auditoria,models.Model):

    """ atributos foraneos"""
    id_militante = models.ForeignKey(Militante, on_delete=models.CASCADE)
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)

    """atributos propios de militante_examen"""
    nota = models.IntegerField()


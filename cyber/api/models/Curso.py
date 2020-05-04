"""
Curso
"""
from django.db import models
from .PlanEstudio import PlanEstudio

from utils.models import Auditoria

class Curso(Auditoria,models.Model):

    """atributos foraneos"""
    id_plan = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)

    """atributos propios de curso"""
    nombre_curso = models.CharField(max_length=45, blank=True, default='')
    sumilla = models.CharField(max_length=300, blank=True, default='')
    docente = models.CharField(max_length=100, blank=True, default='')

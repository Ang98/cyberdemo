"""
Curso
"""
from django.db import models
import PlanEstudio


class Curso(models.Model):

    """atributos foraneos"""
    id_plan = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)

    """atributos propios de curso"""
    nombre_curso = models.CharField(max_length=45, blank=True, default='')
    sumilla = models.CharField(max_length=300, blank=True, default='')
    docente = models.CharField(max_length=100, blank=True, default='')

    """ atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

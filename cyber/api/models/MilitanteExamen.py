"""
Militante Examen
"""
from django.db import models
from .Militante import Militante
from .Examen import Examen


class MilitanteExamen(models.Model):

    """ atributos foraneos"""
    id_militante = models.ForeignKey(Militante, on_delete=models.CASCADE)
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)

    """atributos propios de militante_examen"""
    nota = models.IntegerField()

    """ atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

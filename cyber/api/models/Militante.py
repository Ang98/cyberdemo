"""
Militante
"""
from django.db import models

from .PlanEstudio import PlanEstudio
from .PartidoPolitico import PartidoPolitico

from utils.models import Auditoria

class Militante(Auditoria,models.Model):

    """atributos foraneos militante"""
    usuario=  models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE)
    id_plan = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)
    id_partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)

    """atributos propios de militante"""

    perfil = models.CharField(max_length=45, blank=True, default='')
    cargo = models.CharField(max_length=45, blank=True, default='')
    encargado = models.CharField(max_length=45, blank=True, default='')

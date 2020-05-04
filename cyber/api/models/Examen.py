"""
Examen
"""
from django.db import models

from utils.models import Auditoria

class Examen(Auditoria,models.Model):

    """atributos propios de examen"""
    tipo = models.CharField(max_length=45, blank=True, default='')
    responsable = models.CharField(max_length=45, blank=True, default='')


"""
Eseg JNE
"""
from django.db import models

from utils.models import Auditoria

class EsegJNE(Auditoria,models.Model):

    """atributos propios de eseg_jne"""
    estado = models.IntegerField()
    dni_responsable = models.CharField(max_length=45, blank=True, default='')
    apellidos = models.CharField(max_length=100, blank=True, default='')
    nombres = models.CharField(max_length=100, blank=True, default='')
    sugerencia = models.CharField(max_length=400, blank=True, default='')
    observacion = models.CharField(max_length=400, blank=True, default='')


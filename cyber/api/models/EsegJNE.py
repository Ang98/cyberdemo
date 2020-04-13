"""
Eseg JNE
"""
from django.db import models


class EsegJNE(models.Model):

    """atributos propios de eseg_jne"""
    estado = models.IntegerField()
    dni_responsable = models.CharField(max_length=45, blank=True, default='')
    apellidos = models.CharField(max_length=100, blank=True, default='')
    nombres = models.CharField(max_length=100, blank=True, default='')
    sugerencia = models.CharField(max_length=400, blank=True, default='')
    observacion = models.CharField(max_length=400, blank=True, default='')

    """atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')

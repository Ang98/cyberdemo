"""Auditoria"""

from django.db import models 

class Auditoria(models.Model):
    """Modelo de Auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='')
    
    class Meta:
        """meta opcion"""
        abstract = True
        get_latest_by = 'fecha_registro'
        ordering = ['-fecha_registro', '-fecha_modificacion']
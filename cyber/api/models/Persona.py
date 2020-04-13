"""
Persona
"""
from django.db import models


class Persona(models.Model):

    """atributos propios de persona"""
    nombres = models.CharField(max_length=40, blank=True,)
    apellido_paterno = models.CharField(
        max_length=20, blank=True, default='nombre')
    apellido_materno = models.CharField(
        max_length=20, blank=True, default='appellido_p')
    dni = models.CharField(max_length=15, blank=True, default='apellido_m')
    correo = models.EmailField()
    telefono = models.IntegerField()
    usuario = models.CharField(max_length=40, blank=True, default='user')
    contraseña = models.CharField(max_length=40, blank=True, default='pass')

    """ atributos de auditoria"""
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(
        max_length=45, blank=True, default='user')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(
        max_length=45, blank=True, default='user')

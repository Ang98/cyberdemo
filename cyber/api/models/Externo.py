"""
Externo
"""

from django.db import models

from utils.models import Auditoria


class Externo(Auditoria,models.Model):

    """ atributos propios de externo"""
    usuario=  models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=400, blank=True, default='')

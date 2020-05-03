"""modelo de usuario"""

from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


from utils.models import Auditoria

class Usuario(Auditoria,AbstractUser):
    """modelo de ususario"""
    
    dni = models.CharField(unique=True,max_length=15, blank=True, default='00000000')

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)


    is_militante = models.BooleanField(default=False)
    is_externo = models.BooleanField(default=False)
    is_administrador = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
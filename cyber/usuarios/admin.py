"""Admin de usuarios"""

from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('username','is_staff','is_militante','is_externo','is_administrador')
    list_filter = ('is_militante','is_externo','is_administrador','is_staff')

admin.site.register(Usuario, UsuarioAdmin)
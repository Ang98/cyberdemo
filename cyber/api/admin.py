from django.contrib import admin

# Register your models here.

from .models.Externo import Externo
from .models.Administrador import Administrador
from .models.Militante import Militante


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display= ('id','usuario','cargo')


@admin.register(Externo)
class ExternoAdmin(admin.ModelAdmin):
    list_display= ('id','usuario','descripcion')

@admin.register(Militante)
class MilitanteAdmin(admin.ModelAdmin):
    list_display= [field.name for field in Militante._meta.get_fields()]




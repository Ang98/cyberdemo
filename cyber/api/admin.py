from django.contrib import admin

# Register your models here.

from .models.Externo import Externo
from .models.Administrador import Administrador




@admin.register(Externo)
class ExternoAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion')


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display= ('id','cargo')


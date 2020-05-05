"""Admin de usuarios"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class UsuarioAdmin(UserAdmin):
    list_display = ('id', 'username', 'is_staff',
                    'is_militante', 'is_externo', 'is_administrador')
    list_filter = ('is_militante', 'is_externo',
                   'is_administrador', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email',)}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Datos de Usuario'), {'fields': ('dni', 'phone_number',)}),
        (('Tipo de Usuario'), {'fields': ('is_externo','is_administrador','is_militante',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','password1','password2','dni', 'phone_number', 'email', )}
         ),
    )
    


admin.site.register(Usuario, UsuarioAdmin)

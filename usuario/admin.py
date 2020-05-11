from django.contrib import admin
from usuario.models import Rol, Estado, Usuario, Mascota

# Register your models here.
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'estado')
    #filter_horizontal = ('estado', )

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado')

class RolAdmin(admin.ModelAdmin):
    list_display = ('id', 'rol')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'correo', 'rol')

admin.site.register(Rol, RolAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Mascota, MascotaAdmin)
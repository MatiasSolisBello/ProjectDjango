from django.forms import ModelForm
from .models import Usuario, Mascota

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut','nombre', 'correo', 'password', 'rol']

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = ['foto', 'nombre', 'raza', 'descripcion', 'estado', 'rut']
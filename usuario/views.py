from django.shortcuts import render
#Permite listar 
from .models import Usuario
from .models import Mascota

# Create your views here.
def index(request):
    return render(request, 'usuario/index.html')

def mascota(request):
    mascota = Mascota.objects.all() #Permite listar
    return render(request, 'usuario/mascota.html', {'mascota':mascota})

def usuario(request):
    usuario = Usuario.objects.all() #Permite listar
    return render(request, 'usuario/usuario.html', {'usuario':usuario}) 


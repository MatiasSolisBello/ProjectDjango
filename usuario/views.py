from django.shortcuts import render, redirect
from .models import Usuario, Mascota
from django.contrib import messages
from .forms import UsuarioForm

def index(request):
    return render(request, 'usuario/index.html')

#
#----------CRUD DE USUARIOS----------
#

#Permite listar
def usuario(request):
    usuario = Usuario.objects.all() 
    var = {'usuario':usuario}
    return render(request, 'usuario/usuario.html', var) 

def usuario_agregar(request):
    form = UsuarioForm()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/usuario')
    return render(request, 'usuario/usuario_agregar.html', {'form': form}) 

def usuario_eliminar(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    mensaje ="ELIMINADO!!"
    messages.success(request, mensaje)
    return redirect('usuario')
    
def usuario_actualizar(request, id):
    instancia = Usuario.objects.get(id=id)
    form = UsuarioForm(instance=instancia)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/usuario')
    return render(request, 'usuario/usuario_actualizar.html',{'form': form} ) 


    
#
#----------CRUD DE MASCOTAS----------
#
def mascota(request):
    mascota = Mascota.objects.all()
    var = {'mascota':mascota}
    return render(request, 'usuario/mascota.html', var)

def mascota_agregar(request):
    #usuario = Usuario.objects.all()
    var = {'mascota':mascota}
    return render(request, 'mascota/mascota_agregar.html', var) 

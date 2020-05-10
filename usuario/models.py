from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    password = models.CharField(max_length=200)
    rol = [
        ('ADM', 'Admin'),
        ('ADO', 'Adoptante'),
    ]

class Mascota(models.Model):
    foto = models.ImageField(upload_to = 'tmp')
    nombre = models.CharField(max_length=200)
    raza = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = [
        ('R', 'Rescatado'),
        ('D', 'Disponible'),
        ('A', 'Adoptado'),
    ]
    rut = models.ManyToManyField(Usuario)
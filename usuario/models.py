from django.db import models

# Create your models here.
class Rol(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    rol = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.rol

class Usuario(models.Model):
    rut = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    password = models.CharField(max_length=200)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    estado = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.estado


class Mascota(models.Model):
    foto = models.ImageField(upload_to = 'tmp')
    nombre = models.CharField(max_length=200)
    raza = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    rut = models.ForeignKey('Usuario', on_delete=models.CASCADE)

# Generated by Django 3.0.4 on 2020-05-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='tmp')),
                ('nombre', models.CharField(max_length=200)),
                ('raza', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('rut', models.ManyToManyField(to='usuario.Usuario')),
            ],
        ),
    ]

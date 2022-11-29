from django.db import models
import datetime 
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# # Create your models here.
# class Persona(models.Model):

#     nombre = models.CharField(max_length=40, default="")
#     apellido = models.CharField(max_length=40, default="")
#     edad = models.IntegerField(default=0)
#     fecha_nacimiento = models.DateField()
#     email = models.EmailField()
#     dni = models.CharField(max_length=8)

#     def __str__(self):
#         return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Edad:{self.edad}, Fecha Nacimiento:{self.fecha_nacimiento}, Correo: {self.email} y DNI: {self.dni}'

class Posteo(models.Model):

    titulo = models.CharField(max_length=50, default="")
    fecha = models.DateField()
    imagen = models.ImageField()
    texto = models.CharField(max_length=8000, default="")




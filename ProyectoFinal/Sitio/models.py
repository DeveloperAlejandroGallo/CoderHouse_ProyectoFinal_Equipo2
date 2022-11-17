from django.db import models
import datetime 


# Create your models here.
class Persona(models.Model):

    nombre = models.CharField(max_length=40, default="")
    apellido = models.CharField(max_length=40, default="")
    edad = models.IntegerField(default=0)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    dni = models.CharField(max_length=8)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Edad:{self.edad}, Fecha Nacimiento:{self.fecha_nacimiento}, Correo: {self.email} y DNI: {dni}'

class Curso(models.Model):
    
    nombre = models.CharField(max_length=40, default="")
    codigo = models.IntegerField()

    def __str__(self) -> str:
        return f'Curso: {self.nombre} - Codigo {self.codigo}'

class Profesor(models.Model): 

    nombre = models.CharField(max_length=40, default="")
    apellido = models.CharField(max_length=40, default="")
    edad = models.IntegerField(default=0)
    profesion =  models.CharField(max_length=40, default="")
    email = models.EmailField()
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Edad:{self.edad}, Profesion:{self.profesion}, Correo: {self.email}'

class Posteo(models.Model):

    titulo = models.CharField(max_length=50, default="")
    fecha = models.DateField()
    # imagen = models.ImageField()
    texto = models.CharField(max_length=8000, default="")

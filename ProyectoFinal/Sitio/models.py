from django.db import models
import datetime

# Create your models here.
class Persona(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField()




class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()

    def __str__(self) -> str:
        return super().__str__(f'Curso: {self.nombre} - Codigo {self.codigo}')

class Profesor(models.Model): 

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    profesion =  models.CharField(max_length=40)
    email = models.EmailField()


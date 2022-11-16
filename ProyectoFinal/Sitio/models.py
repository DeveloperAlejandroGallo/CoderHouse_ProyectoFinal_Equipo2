from django.db import models
import datetime

# Create your models here.
class Persona(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField()


class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()

class Profesor(models.Model): 

    nombre = models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad = models.IntegerField()
    profesion =  models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Edad:{self.edad},Profesion:{self.profesion}, Correo: {self.email}'


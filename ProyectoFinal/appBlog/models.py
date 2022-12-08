from django.db import models
import datetime 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    fecha = models.DateField()
    imagen = models.ImageField()
    texto = models.TextField()
    likes = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.fecha} | {self.titulo} | {self.subtitulo}'


class Comment(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_padre = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    comentario = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return f'{self.post_padre.titulo} | {self.usuario} | {self.titulo}'

class Contact(models.Model):
    nombre = models.CharField(max_length=250)
    email = models.EmailField()
    asunto = models.CharField(max_length=250)
    mensaje = models.TextField(max_length=3000)

    def __str__(self):
        return self.email
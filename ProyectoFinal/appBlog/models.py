from django.db import models
import datetime 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField()
    texto = models.TextField()

    def __str__(self) -> str:
        return f'{self.fecha} | {self.titulo} | {self.subtitulo}'


class Comment():
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_padre = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()

    def __str__(self):
        return f'{self.post_padre.titulo} | {self.usuario} | {self.titulo}'

from django import forms
from django.utils import timezone

class PostCrearForm(forms.Form):
    usuario = forms.CharField(max_length=50)
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    fecha = forms.DateField()
    imagen = forms.ImageField()
    texto = forms.Textarea()

class PostCommentForm(forms.Form):
    usuario = forms.CharField(max_length=50)
    titulo = forms.CharField(max_length=50)
    fecha = forms.DateTimeField()
    post = forms.Textarea()





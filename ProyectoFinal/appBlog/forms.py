from django import forms

class PostCrearForm(forms.Form):
    usuario = forms.CharField(max_length=50)
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    fecha = forms.DateField(auto_now_add=True)
    imagen = forms.ImageField()
    texto = forms.Textarea()

class PostCommentForm(forms.Form):
    usuario = forms.CharField(max_length=50)
    titulo = forms.CharField(max_length=50)
    fecha = forms.DateTimeField(auto_now_add=True)
    post = forms.Textarea()





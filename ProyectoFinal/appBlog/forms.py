from django import forms
from django.utils import timezone
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from appBlog.models import Post
from django.contrib.auth.models import User
#from .models import Contact

class PostCrearForm(forms.Form):
    usuario = forms.CharField(disabled=True)
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    fecha = forms.DateField()
    imagen = forms.ImageField()
    cuerpo = forms.CharField(widget=forms.Textarea)
    likes = forms.IntegerField()
    class Meta:
        model = Post
        fields = ['usuario','titulo','subtitulo','fecha','imagen','cuerpo','likes']

class PostCommentForm(forms.Form):
    usuario = forms.CharField(max_length=50)
    titulo = forms.CharField(max_length=50)
    fecha = forms.DateTimeField()
    cuerpo = forms.CharField(widget=forms.Textarea)

#class ContactForm(forms.Form):
#    email = forms.EmailField()
#    asunto = forms.CharField(max_length=250)
#    mensaje = forms.CharField(widget=forms.Textarea)
# COMENTO PARA PROBAR OTRO METODO



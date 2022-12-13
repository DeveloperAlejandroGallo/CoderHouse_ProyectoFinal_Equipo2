from django import forms
from django.utils import timezone
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from appBlog.models import Post
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget


#from .models import Contact

class PostCrearForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    fecha = forms.DateField(widget=AdminDateWidget)
    imagen = forms.ImageField(required=False)
    cuerpo = forms.CharField(widget=forms.Textarea)



class PostCommentForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    fecha = forms.DateTimeField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    cuerpo = forms.CharField(widget=forms.Textarea)


class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','subtitulo','fecha','imagen','cuerpo']

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateField(widget=AdminDateWidget),
            'imagen': forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
        }


#class ContactForm(forms.Form):
#    email = forms.EmailField()
#    asunto = forms.CharField(max_length=250)
#    mensaje = forms.CharField(widget=forms.Textarea)
# COMENTO PARA PROBAR OTRO METODO



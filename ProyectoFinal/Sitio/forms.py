from django import forms

class CrearProfesorForm(forms.Form):

    nombre=forms.CharField(min_length=4, max_length=15)
    apellido=forms.CharField(min_length=2, max_length=15)
    edad=forms.IntegerField()
    profesion=forms.CharField(min_length=4, max_length=15)
    email=forms.EmailField()


class CrearCursoForm(forms.Form):

    nombre=forms.CharField(min_length=4, max_length=15)
    codigo=forms.IntegerField()


class CrearPersonaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    email = forms.EmailField()
    dni = forms.CharField(max_length=8)

class CrearPosteoForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    fecha = forms.DateField()
    # imagen = forms.ImageField()
    texto = forms.CharField(max_length=8000)
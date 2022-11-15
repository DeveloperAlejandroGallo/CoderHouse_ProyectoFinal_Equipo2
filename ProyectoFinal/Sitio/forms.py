from django import forms

class CrearProfesorForm(forms.Form):

    nombre=forms.CharField(min_length=4, max_length=15)
    edad=forms.IntegerField()
    profesion=forms.CharField(min_length=4, max_length=15)
    email=forms.EmailField()



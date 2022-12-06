from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Nombre de Usuario")
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
        help_text = {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField()
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label='Apellido')
    password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)
    about = forms.CharField(widget=forms.Textarea, label='Acerca de ti...', required=False)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields =[
            'email',
            'nombre',
            'apellido',
            'password1',
            'password2',
            'about',
            'avatar'
        ]
        help_text = {k: "" for k in fields}


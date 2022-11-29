from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CrearPosteoForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    fecha = forms.DateField()
    # imagen = forms.ImageField()
    texto = forms.CharField(max_length=8000)


class SignUpForm(UserCreationForm):

    class meta:
        model = User
        fields =[
            'username'
            'email'
            'password1'
            'password2'
        ]

class UserEditForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}


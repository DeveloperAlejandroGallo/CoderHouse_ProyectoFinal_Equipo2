from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class UserRegisterForm(UserCreationForm):

#     username = forms.CharField(label="Nombre de Usuario")
#     email = forms.EmailField(label="Correo Electronico")
#     first_name = forms.CharField(label="Nombre")
#     last_name = forms.CharField(label='Apellido')
#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
#         help_text = {k: "" for k in fields}

# class UserEditForm(UserCreationForm):

#     email = forms.EmailField(disabled=True)
#     first_name = forms.CharField(label="Nombre")
#     last_name = forms.CharField(label='Apellido')
#     password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)
#     # about = forms.Textarea()
#     # avatar = forms.ImageField()

#     class Meta:
#         model = User
#         fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
#         help_text = {k: "" for k in fields}


class CustomUserCreationForm(UserCreationForm):

        class Meta :
            model = User
            fields = ['username' ,'first_name', 'last_name', 'email','password1', 'password2'] 

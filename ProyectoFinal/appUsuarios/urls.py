from django.contrib import admin
from django.urls import path
from appUsuarios.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', user_login, name='Login'),
    path('accounts/singup/', user_signup, name='SignUp'),
    path('accounts/logout/', LogoutView.as_view(template_name='appUsuarios/logout.html'), name='Logout'),

    path('accounts/edit_user/', user_edit, name="Editar Perfil"),

    path('accounts/profile/<usuario>', user_view, name='Ver Perfil'),
]
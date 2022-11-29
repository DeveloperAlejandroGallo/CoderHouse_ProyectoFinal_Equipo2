from django.contrib import admin
from django.urls import path
from Sitio import views
from django.contrib.auth import login,logout

urlpatterns = [
    path('',views.inicio),
    path('index.html', views.inicio),
    path('blog.html', views.blog),
    path('about.html', views.about),
    path('post-details.html', views.post_details),
    path('contact.html', views.contact),
    path('support.html', views.support),
    path('ingresar.html',views.login_request),
    path('registrarse.html',views.SignUpView.as_view(), name='Registrarse'),
    path('admin/', admin.site.urls, name='Admin')
]
from django.contrib import admin
from django.urls import path
from appBlog.views import *
from django.contrib.auth import login,logout

urlpatterns = [
    path('',inicio, name='Index'),
    path('about.html', about, name = 'About'),
    path('contact.html', contact, name='Contact'),
    path('post_create.html', post_create, name='Post Create'),
    path('post_details.html', post_details, name='Post Details'),
    path('post_list.html', post_list, name='Post List'),
]
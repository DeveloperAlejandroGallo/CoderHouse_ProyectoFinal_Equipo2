from django.contrib import admin
from django.urls import path, include
from appBlog.views import *
from django.contrib.auth import login,logout 
#from .views import contactView, successView
# from .views import successView

urlpatterns = [
    path('',inicio, name='Index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('about', about, name = 'About'),
    path('contact', contact, name='Contact'),
    path('post_create', post_create, name='Post Create'),
    path('post_edit/<pk>', post_edit, name='Post Edit'),
    path('post_list', post_list, name='Post List'),
    path('post_find', post_find, name='Post Find'),
    #path('contact', contactView, name='contact'),
    #path('success', successView, name='success'),
] 

    

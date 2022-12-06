from django.contrib import admin
from django.urls import path
from appBlog.views import *
from django.contrib.auth import login,logout

urlpatterns = [
    path('',inicio, name='Index'),
    path('about', about, name = 'About'),
    path('contact', contact, name='Contact'),
    path('post_create', post_create, name='Post Create'),
    path('post_details/<post>', post_details, name='Post Details'),
    path('post_list', post_list, name='Post List'),
    path('post_find', post_list, name='Post Find'),
]
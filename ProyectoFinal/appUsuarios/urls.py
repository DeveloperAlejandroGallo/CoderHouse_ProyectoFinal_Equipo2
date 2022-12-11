from django.contrib import admin
from django.urls import path
from appUsuarios.views import registro,open_inbox,user_view,chatting,open_profile,open_user_profile
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/',registro, name='signup'),
    # path('accounts/login/', user_login, name='Login'),
    # path('accounts/singup/', user_signup, name='SignUp'),
    path('accounts/logout/', LogoutView.as_view(template_name='appUsuarios/logout.html'), name='Logout'),


    # path('accounts/profile/<usuario>', user_view, name='Profile'),
    # path('accounts/edit_user/<usuario>', user_edit, name="Edit Profile"),('accounts/addavatar/', add_avatar, name='addAvatar'),
    path('accounts/profile/', open_profile, name='Profile'),
    path('accounts/userprofile/<usuario>', open_user_profile, name='OpenProfile'),
    path('chat/<usuario>', chatting, name='Chat'),
    path('inbox/', open_inbox, name='Inbox'),
]
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from appUsuarios.forms import *
from appUsuarios.models import *


# Create your views here.



def user_login(request):

    if request.method=='POST':
        
        loginForm = AuthenticationForm(request,data = request.POST)

        if loginForm.is_valid():
            usuario = loginForm.cleaned_data.get('username')
            contra = loginForm.cleaned_data.get('password')

            user = authenticate(username=usuario ,password=contra)
            
            if user is not None:
                login(request,user)
                return render (request,'appBlog/index.html', {'user':usuario,'form':loginForm})
            else:
                return render (request,'appUsuarios/login.html',{'mensaje':f'El usuario no existe'})
        else:
            loginForm = AuthenticationForm()
            return render (request,'appUsuarios/login.html',{'form':loginForm,'mensaje':f'Usuario o Contraseña incorrectos'})

    loginForm = AuthenticationForm()
    return render (request,'appUsuarios/login.html',{'form':loginForm})

def user_signup(request):

    if( request.method == "POST"):

        signupForm = UserRegisterForm(request.POST)

        if(signupForm.is_valid()):
            signupForm.save()

            return redirect('Login')

        else:
            signupForm = UserRegisterForm()
            return render(request, 'appUsuarios/signup.html', {"signupForm": signupForm, "mensaje": ['Datos ingresados Erróneos']})

    else:
        signupForm = UserRegisterForm()
        return render(request, 'appUsuarios/signup.html', {"signupForm": signupForm}) 

@login_required
def user_edit(request):

    user = request.user

    if request.method == 'POST':
         
        userEditForm = UserEditForm(request.POST)

        if (userEditForm.is_valid()):

            data = userEditForm.cleaned_data

            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.password1 = data["password1"]
            user.password2 = data["password2"]

            user.save()

            userData = UserData.objects.filter(user=user)

            if len(userData) > 0:

                userData = userData[0]

                userData.avatar = data['avatar']
                userData.aboutMe = data['aboutMe']
                userData.github = data['github']
            else:
                userData = UserData(
                    user= user, 
                    avatar=data['avatar'], 
                    aboutMe=data['aboutMe'], 
                    github=data['github'])
            
            userData.save()

            return redirect('Index')

        else:

            userEditForm = UserEditForm()

            return render(request, 'appUsuarios/edit_user.html', {"userEditForm": userEditForm, "mensaje": ['Datos ingresados inválidos.'], 'img':img})

    else: 

        userEditForm = UserEditForm(initial={'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})

        return render(request, 'appUsuarios/edit_user.html', {"userEditForm": userEditForm})

@login_required
def user_view(request):

    user = request.user
    userData = UserData.objects.filter(user=user)

    if(len(userData) == 0):
        return render('appUsuarios/profile.html', {'user':user,'mensaje':"Informacion no disponible aun."})
    else:
        return render('appUsuarios/profile.html', {'user':user,'userData':userData})

        

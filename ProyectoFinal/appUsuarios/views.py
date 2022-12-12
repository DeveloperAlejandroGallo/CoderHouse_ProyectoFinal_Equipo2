from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from appUsuarios.forms import CustomUserCreationForm ,Avatar_form,Chat_form
from appUsuarios.models import *
from django.contrib import messages 
from appUsuarios.models import Avatar, UserAbout , Chat 




# Create your views here.


def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method =='POST': 
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request,'te has registrado correctamente')
            return redirect('Index')
        data['form']= formulario
    return render (request, 'registration/signup.html', data)
    

# def user_login(request):
#     template_name = 'login.html'
#     return render(request,'registration/login.html')

#     if request.method=='POST':
        
#         loginForm = AuthenticationForm(request,data = request.POST)

#         if loginForm.is_valid():
#             email = loginForm.cleaned_data.get('email')
#             contra = loginForm.cleaned_data.get('password')

#             user = authenticate(email=email ,password=contra)
            
#             if user is not None:
#                 login(request,user)
#                 return render (request,'appBlog/index.html', {'email':email,'form':loginForm})
#             else:
#                 return render (request,'appUsuarios/login.html',{'mensaje':'El usuario no existe'})
#         else:
#             loginForm = AuthenticationForm()
#             return render (request,'appUsuarios/login.html',{'form':loginForm,'mensaje':'Usuario o Contraseña incorrectos'})

#     loginForm = AuthenticationForm()
#     return render (request,'appUsuarios/login.html',{'form':loginForm})

# def user_signup(request):

#     if( request.method == "POST"):

#         signupForm = UserRegisterForm(request.POST)

#         if(signupForm.is_valid()):
#             signupForm.save()

#             return redirect('Login')

#         else:
#             signupForm = UserRegisterForm()
#             return render(request, 'appUsuarios/signup.html', {"signupForm": signupForm, "mensaje": ['Datos ingresados Erróneos']})

#     else:
#         signupForm = UserRegisterForm()
#         return render(request, 'appUsuarios/signup.html', {"signupForm": signupForm}) 

# @login_required
# def user_edit(request):

#     user = request.user

#     if request.method == 'POST':
         
#         userEditForm = UserEditForm(request.POST)

#         if (userEditForm.is_valid()):

#             data = userEditForm.cleaned_data

#             user.email = data["email"]
#             user.first_name = data["first_name"]
#             user.last_name = data["last_name"]
#             user.password1 = data["password1"]
#             user.password2 = data["password2"]

#             user.save()

#             userData = UserData.objects.filter(user=user)

#             if len(userData) > 0:

#                 userData = userData[0]

#                 userData.avatar = data['avatar']
#                 userData.aboutMe = data['aboutMe']
#                 userData.github = data['github']
#             else:
#                 userData = UserData(
#                     user= user, 
#                     avatar=data['avatar'], 
#                     aboutMe=data['aboutMe'], 
#                     github=data['github'])
            
#             userData.save()

#             return redirect('Index')

#         else:

#             userEditForm = UserEditForm()

#             return render(request, 'appUsuarios/edit_user.html', {"userEditForm": userEditForm, "mensaje": ['Datos ingresados inválidos.'], 'img':img})

#     else: 

#         userEditForm = UserEditForm(initial={'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})

#         return render(request, 'appUsuarios/edit_user.html', {"userEditForm": userEditForm})



@login_required
def add_avatar(request):

    if request.method == 'POST':

        miAvatar = Avatar_form(request.POST, request.FILES)

        if miAvatar.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            file = miAvatar.cleaned_data

            if len(avatar) > 0:

                avatar = avatar[0]
                avatar.imagen = file['img']
                avatar.save()

                avatar = Avatar.objects.filter(user=request.user)

                img = avatar[0].imagen.url

            else:

                avatar = Avatar(user=usuario, imagen=miAvatar.cleaned_data['img'])
                avatar.save()

                img = None

        return render(request, 'appBlog/index.html', {'img':img})

    else:

        miAvatar = Avatar_form()

        img = None
        
        return render(request, 'appUsuarios/addavatar.html', {'miAvatar': miAvatar, 'img': img})


@login_required
def open_user_profile(request):
 
    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:

        imgprofile = avatar[0].imagen.url

    else:

        imgprofile = None

    aboutuser = UserAbout.objects.filter(user=request.user)

    if len(aboutuser) > 0:

        bio = aboutuser[0].bio
        instagram = aboutuser[0].instagram
        facebook = aboutuser[0].facebook
        twitter = aboutuser[0].twitter

    else:
    
        bio = 'Información no disponible aún.'
        instagram = None
        facebook = None
        twitter = None

    if request.user.username:

        avatar1 = Avatar.objects.filter(user=request.user)

        if len(avatar1) > 0:

            img = avatar1[0].imagen.url

        else:

            img = None
    
    else:

        img = None

    return render(request, 'appUsuarios/profile.html', {'img': img, 'user': request.user, 'imgprofile': imgprofile, 'bio':bio, 'instagram':instagram, 'facebook':facebook, 'twitter':twitter})

@login_required
def chatting(request, usuario):

    receiver = User.objects.get(username=usuario)

    avatar = Avatar.objects.filter(user=request.user)

    messages = Chat.objects.all()

    if len(avatar) > 0:

        img = avatar[0].imagen.url

    else:

        img = None

    if request.method == 'POST':

        miMessage = Chat_form(request.POST)

        if miMessage.is_valid():

            message = Chat(writer=request.user, body=miMessage.cleaned_data['body'], recipient=receiver)

            message.save()

            miMessage = Chat_form()

            return render(request, 'appUsers/chat.html', {'img': img, 'user':request.user, 'receiver': receiver, 'messages':messages, 'miMessage': miMessage})

    else:

        miMessage = Chat_form()

    return render(request, 'appUsers/chat.html', {'img': img, 'user':request.user, 'receiver': receiver, 'messages':messages, 'miMessage': miMessage})

@login_required
def open_inbox(request):

    activechats = Chat.objects.all()

    listchats = []

    for chat in activechats:

        if chat.recipient != request.user or chat.recipient == request.user:


            if chat.recipient == request.user and chat.writer not in listchats:

                listchats.append(chat.writer)
            
            elif chat.recipient != request.user and chat.recipient.username not in listchats:

                listchats.append(chat.recipient.username)


    return render(request, 'appUsers/inbox.html', {'listchats':listchats, 'activechats':activechats})

        
# class SignUpView(CreateView):

#     form_class = SignUpForm
#     success_url = reverse_lazy('index.html')
#     template_name = 'registrarse.html'


# class AdminLoginView(LoginView):
#     template_name = 'ingresar.html'

# class AdminLogoutView(LogoutView):
#     template_name = 'cerrar_sesion.html'
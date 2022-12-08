from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from appBlog.forms import *
from appBlog.models import *
from appUsuarios.models import *


def inicio(request):

    if request.user.username:

        userData = UserData.objects.filter(user=request.user)

        user = request.user
        return render(request,'appBlog/index.html', {'user':user,'userData':userData}) 
    else:
        return render(request,'appBlog/index.html', {'user':None,'userData':None}) 



def about(request):
    return render(request,'appBlog/about.html') 

def contact(request):
    return render(request,'appBlog/contact.html') 


#Ver un post solo que tiene la opcion de hacer comentarios
def post_details(request, post):
    return render(request,'appBlog/post_details.html') 

def post_create(request):
    return render(request, 'appBlog/post_create.html')

def post_list(request):
    return render(request,'appBlog/post_list.html')

def post_find(request):
    return render(request,'appBlog/post_find.html')


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            asunto = form.cleaned_data["asunto"]
            email = form.cleaned_data["email"]
            mensaje = form.cleaned_data['mensaje']
            try:
                send_mail(asunto, mensaje, email, ["aleveliz75@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Inválido.")
            return redirect("Enviado")
    return render(request, "contact.html", {"form": form})

def successView(request):
    return HttpResponse("Enviado! Gracias por tu mensaje!.")

# class SignUpView(CreateView):

#     form_class = SignUpForm
#     success_url = reverse_lazy('index.html')
#     template_name = 'registrarse.html'


# class AdminLoginView(LoginView):
#     template_name = 'ingresar.html'

# class AdminLogoutView(LogoutView):
#     template_name = 'cerrar_sesion.html'


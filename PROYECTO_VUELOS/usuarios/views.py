from django.shortcuts import render
from django.urls import reverse
from django.http import request, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth

# Create your views here.
def index(request):
    if not request.user.is_authenticated: # Si el usuario no esta loguedo sera enviado al Login
        return HttpResponseRedirect(reverse('usuarios:login'))
    return render(request, 'usuarios/user.html')

def login_view(request):
    if request.method == 'POST':
        nombreusuario= request.POST['nombreusuario']    # Accede a los datos "nombreusuario" y "pasword" del form
        password= request.POST['password']
        usuario= authenticate(request, nombreusuario= nombreusuario, password= password)
        if usuario:                                     # si usuario es objeto usuario, manda a loguerse y redirije al index
            login(request, usuario)
            return HttpResponseRedirect(reverse('usuarios:index'))
        else:                                           # Sino, retorna a la pagina Login con nuevo contexto
            return render(request, 'usuarios/login.html',{'mensaje':'Credenciales no válidas'})
    return render(request, 'usuarios/login.html')

def logout_view(request):
    #pass -> Indica que no haga nada
    logout(request)
    return render(request, 'usuarios/login.html',
            {'mensaje':'Se ha desconectado.'})

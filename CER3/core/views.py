from django.shortcuts import render, redirect
from .models import Evento
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def home(request):
    title = "Home"
    segmentos = Evento.SEGMENTO_CHOICES
    segmento_seleccionado = request.GET.get("segmento")
    print(segmento_seleccionado)
    if segmento_seleccionado == 'Todos' or segmento_seleccionado is None:
        eventos = Evento.objects.all()
    else:
        for segmento in segmentos:
            print(segmento)
            if str(segmento) == str(segmento_seleccionado):
                print("ola")
                eventos = Evento.objects.filter(segmento=segmento[0])
                print(eventos)
                break
        
    data = {
        "title": title,
        "eventos": eventos,
        "segmentos" :segmentos,
    }
    return render(request, 'core/home.html', data)

def cerrarSesion(request):
    logout(request)
    return redirect('home')

def iniciarSesion(request):
    if request.method == 'GET':
        data = {
            'form': AuthenticationForm
        }
        return render(request, 'core/login.html', data)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            data = {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            }
            return render(request, 'core/login.html', data)
        else:
            login(request, user)
            return redirect('home')

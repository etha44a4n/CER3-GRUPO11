from django.shortcuts import render, redirect
from .models import Evento, Segmento
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def home(request):
    title = "Home"
    segmentos = Segmento.objects.all()
    segmento_seleccionado = request.GET.get("segmento")
    tipos = Evento.TIPO_CHOICES
    tipo_seleccionado = request.GET.get("tipo")
    
    if (segmento_seleccionado == 'Todos' or segmento_seleccionado is None) and (tipo_seleccionado == 'Todos' or tipo_seleccionado is None):
        eventos = Evento.objects.all()
    else:
        if segmento_seleccionado == 'Todos' or segmento_seleccionado is None:
            for tipo in tipos:
                if str(tipo[0]) == str(tipo_seleccionado):
                    eventos = Evento.objects.filter(tipo=tipo[0])
                    break
        
        elif tipo_seleccionado == 'Todos' or tipo_seleccionado is None:
            segmento_a_filtrar = Segmento.objects.get(nombre=segmento_seleccionado)
            eventos = Evento.objects.filter(segmento=segmento_a_filtrar)

        else:
            segmento_a_filtrar = Segmento.objects.get(nombre=segmento_seleccionado)
            for tipo in tipos:
                if tipo[0] == tipo_seleccionado:
                    eventos = Evento.objects.filter(segmento=segmento_a_filtrar, tipo=tipo[0])
                    break
            
   
    data = {
        "title": title,
        "eventos": eventos,
        "segmentos" :segmentos,
        "tipos": tipos,
        "segmento_seleccionado": segmento_seleccionado,
        "tipo_seleccionado": tipo_seleccionado,
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
        print(authenticate(request, username='percy', password='1234'))
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(authenticate(request, username='percy', password='1234'))
        if user is None:
            data = {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            }
            return render(request, 'core/login.html', data)
        else:
            login(request, user)
            return redirect('home')

from django.shortcuts import render, redirect
from .models import Evento, Segmento
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone

def home(request):
    title = "Home"
    segmentos = Segmento.objects.all()
    segmento_seleccionado = request.GET.get("segmento")
    tipos = Evento.TIPO_CHOICES
    tipo_seleccionado = request.GET.get("tipo")
    segmento_usuario = None
    username = 'Anónimo'
    eventos_segmento = None
    fecha_usuario = timezone.now()
    segmento_dev = None
    if request.user.is_authenticated:
        if (str(request.user.tipo_cuenta)== 'Developer'):
            segmento_dev = request.user.tipo_cuenta
        username = request.user.username
        if (str(request.user.tipo_cuenta)== 'Jefe de Carrera' or str(request.user.tipo_cuenta) == 'Profesor'):
            segmento_usuario = request.user.tipo_cuenta
            eventos_segmento = Evento.objects.filter(segmento=segmento_usuario, fechaInicio__gte=timezone.now()).order_by('fechaInicio')[:3]

    if (segmento_seleccionado == 'Todos' or segmento_seleccionado is None) and (tipo_seleccionado == 'Todos' or tipo_seleccionado is None):
        eventos = Evento.objects.filter(fechaInicio__gte=timezone.now()).order_by('fechaInicio')
    else:
        if segmento_seleccionado == 'Todos' or segmento_seleccionado is None:
            for tipo in tipos:
                if str(tipo[0]) == str(tipo_seleccionado):
                    eventos = Evento.objects.filter(tipo=tipo[0], fechaInicio__gte=timezone.now()).order_by('fechaInicio')
                    break
        
        elif tipo_seleccionado == 'Todos' or tipo_seleccionado is None:
            segmento_a_filtrar = Segmento.objects.get(nombre=segmento_seleccionado)
            eventos = Evento.objects.filter(segmento=segmento_a_filtrar, fechaInicio__gte=timezone.now()).order_by('fechaInicio')

        else:
            segmento_a_filtrar = Segmento.objects.get(nombre=segmento_seleccionado)
            for tipo in tipos:
                if tipo[0] == tipo_seleccionado:
                    eventos = Evento.objects.filter(segmento=segmento_a_filtrar, tipo=tipo[0], fechaInicio__gte=timezone.now()).order_by('fechaInicio')
                    break
            
    data = {
        "title": title,
        "eventos": eventos,
        "segmentos" :segmentos,
        "tipos": tipos,
        "segmento_seleccionado": segmento_seleccionado,
        "tipo_seleccionado": tipo_seleccionado,
        "segmento_usuario": segmento_usuario,
        "username": username,
        "eventos_segmento": eventos_segmento,
        "fecha_usuario": fecha_usuario,
        'segmento_dev': segmento_dev
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

from django.shortcuts import render
from .models import Evento

def home(request):
    title = "Home"
    segmentos = Evento.SEGMENTO_CHOICES
    segmento_seleccionado = request.GET.get("segmento")
    tipos = Evento.TIPO_CHOICES
    tipo_seleccionado = request.GET.get("tipo")
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

    if tipo_seleccionado == 'Todos' or tipo_seleccionado is None:
        eventos = Evento.objects.all()
    else:
        for tipo in tipos:
            print(tipo)
            if str(tipo) == str(tipo_seleccionado):
                print("Tabn el tipo")
                eventos = Evento.objects.filter(tipo=tipo[0])
                print(eventos)
                break        
        
    data = {
        "title": title,
        "eventos": eventos,
        "segmentos" :segmentos,
        "tipos": tipos,
    }
    return render(request, 'core/home.html', data)
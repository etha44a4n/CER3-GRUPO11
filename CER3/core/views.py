from django.shortcuts import render
from .models import Evento

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
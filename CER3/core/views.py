from django.shortcuts import render
from .models import Evento

def home(request):
    title = "Home"
    segmentos = Evento.SEGMENTO_CHOICES
    segmento_seleccionado = request.GET.get("segmento")
    tipos = Evento.TIPO_CHOICES
    tipo_seleccionado = request.GET.get("tipo")
    
    if segmento_seleccionado == 'Todos' or segmento_seleccionado is None:
        eventos = Evento.objects.all()
    else:
        for segmento in segmentos:
            if str(segmento) == str(segmento_seleccionado):
                eventos = Evento.objects.filter(segmento=segmento[0])
                break

    if tipo_seleccionado == 'Todos' or tipo_seleccionado is None:
        eventos = Evento.objects.all()
    else:
        for tipo in tipos:
            if str(tipo) == str(tipo_seleccionado):
                print("Tabn el tipo")
                eventos = Evento.objects.filter(tipo=tipo[0])
                print(eventos)
                break        
    print(segmento_seleccionado, tipo_seleccionado)   
    data = {
        "title": title,
        "eventos": eventos,
        "segmentos" :segmentos,
        "tipos": tipos,
        "segmentoselec": segmento_seleccionado,
        "tiposelec": tipo_seleccionado,
    }
    return render(request, 'core/home.html', data)
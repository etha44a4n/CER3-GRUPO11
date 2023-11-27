from rest_framework import viewsets
from .permissions import IsDeveloper
from core.models import Evento
from .serializers import EventoSerializer
from rest_framework.filters import SearchFilter

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsDeveloper]
    filter_backends = [SearchFilter]
    search_fields = ['fechaInicio' ,'segmento__nombre', 'tipo']


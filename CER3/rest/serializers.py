from rest_framework import serializers 
from core.models import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Evento
        Fields = '__all__'
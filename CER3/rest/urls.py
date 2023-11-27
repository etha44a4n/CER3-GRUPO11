from rest_framework import routers
from .views import EventoViewSet
from django.urls import path, include 

router = routers.DefaultRouter()
router.register(r'evento', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
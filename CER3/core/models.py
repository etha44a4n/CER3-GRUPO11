from django.db import models
from django.contrib.auth.models import AbstractUser

class Segmento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre

class Evento(models.Model):
    TIPO_CHOICES = [
        ("VA","Vacaciones"),
        ("FE","Feriado"),
        ("SS", "Suspensión de actividades"),
        ("SP", "Suspensión de actividades PM"),
        ("PL", "Periodo Lectivo"),
        ("SE", "Suspensión de evaluaciones"),
        ("CE", "Ceremonia"),
        ("ED", "EDDA"),
        ("EV", "Evaluación"),
        ("AY", "Ayudantías"),
        ("HA", "Hito Académico"),
        ("SA", "Secretaría Académica"),
        ("OA", "OAI"),
    ]
    id = models.BigAutoField(primary_key=True)
    fechaInicio = models.DateTimeField(auto_now_add=False)
    fechaTermino = models.DateTimeField(auto_now_add=False)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    segmento = models.ManyToManyField(Segmento)

    def __str__(self) -> str:
        return self.titulo

class TipoUsuario(AbstractUser):
    tipo_cuenta = models.ForeignKey(Segmento, on_delete=models.CASCADE, null=True)


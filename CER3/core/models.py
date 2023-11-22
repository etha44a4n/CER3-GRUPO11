from django.db import models


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

    SEGMENTO_CHOICES = [
        ("CU", "Comunidad USM"),
        ("ES", "Estudiante"),
        ("PR", "Profesor"),
        ("JF","Jefe de Carrera"),
    ]

    fechaInicio = models.DateTimeField(auto_now_add=False)
    fechaTermino = models.DateTimeField(auto_now_add=False)
    titulo = models.CharField(max_length=55)
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    segmento = models.CharField(max_length=2, choices=SEGMENTO_CHOICES)

    def __str__(self) -> str:
        return self.titulo
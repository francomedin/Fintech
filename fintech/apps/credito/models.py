from django.db import models
from django.db.models.enums import Choices

# Create your models here.


class Credito(models.Model):

    OK = 'ok'
    MORA_TEMPRANA = 'Mora Temprana'
    MORA_TARDIA = 'Mora Tardia'

    ESTADOS = (
        (OK, 'Al dia'),
        (MORA_TEMPRANA, 'Atraso > 30 días'),
        (MORA_TARDIA, 'Atraso > 90 dí as')
    )
    monto = models.FloatField()
    fecha_prestamo = models.DateField()
    monto = models.FloatField()
    interes = models.FloatField()
    cuotas = models.IntegerField()
    mora = models.FloatField(default=0)
    activo = models.BooleanField(default=True)
    situacion = models.CharField(max_length=15, choices=ESTADOS, default=OK)

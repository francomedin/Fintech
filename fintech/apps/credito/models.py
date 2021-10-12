from django.db import models
from .managers import CreditoManager
from apps.cliente.models import Cliente
# Create your models here.


class Credito(models.Model):

    OK = 'ok'
    MORA_TEMPRANA = 'Mora Temprana'
    MORA_TARDIA = 'Mora Tardia'
    SITUACION_JUDICIAL = 'Situacion Judicial'

    ESTADOS = (
        (OK, 'Al dia'),
        (MORA_TEMPRANA, 'Atraso entre 1 y 30 días'),
        (MORA_TARDIA, 'Atraso > 30 días'),
        (SITUACION_JUDICIAL, 'Atraso > 90 días')
    )
    titular = models.ForeignKey(Cliente, on_delete=models.PROTECT, default=1)
    capital = models.FloatField()
    fecha_prestamo = models.DateField()
    monto_cuota = models.FloatField(default=0)
    tasa_interes = models.FloatField()
    cant_cuota = models.IntegerField()
    mora = models.FloatField(default=0)
    activo = models.BooleanField(default=True)
    situacion = models.CharField(max_length=20, choices=ESTADOS, default=OK)
    objects = CreditoManager()

    def __str__(self):
        return str(self.titular) + '|| Cuota: $' + str(self.monto_cuota)

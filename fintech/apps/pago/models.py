from apps.credito.models import Cuota
from django.db import models
from .managers import PagoManager
# Create your models here.


class TipoPago(models.Model):
    tipo_pago = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo_pago


class MetodoPago(models.Model):
    metodo_pago = models.CharField(
        max_length=30, verbose_name='Metodo de Pago')

    def __str__(self):
        return self.metodo_pago


class Cobrador(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Pago(models.Model):

    cuota = models.ForeignKey(Cuota, on_delete=models.PROTECT, default=1)
    monto = models.FloatField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=300, blank=True)
    # Tipo de pago: Cuota, cancelacion, embargo/juicio.
    tipo = models.ForeignKey(TipoPago, on_delete=models.PROTECT, default=1)
    # Metodo de pago ej: transferencia
    metodo = models.ForeignKey(MetodoPago, on_delete=models.PROTECT, default=1)
    # Cobrador que recibio el pago. ej. Fulano.
    cobrador = models.ForeignKey(Cobrador, on_delete=models.PROTECT, default=1)
    objects = PagoManager()

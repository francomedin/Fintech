from apps.credito.models import Credito
from django.db import models

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

    monto = models.FloatField()
    fecha = models.DateField()
    credito = models.ForeignKey(Credito, on_delete=models.PROTECT, default=1)
    descripcion = models.CharField(
        max_length=300, blank=True)
    tipo = models.ForeignKey(TipoPago, on_delete=models.PROTECT, default=1)
    metodo = models.ForeignKey(MetodoPago, on_delete=models.PROTECT, default=1)
    cobrador = models.ForeignKey(Cobrador, on_delete=models.PROTECT, default=1)

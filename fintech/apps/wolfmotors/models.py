from django.db import models
from django.db.models.deletion import PROTECT
from apps.pago.models import Cobrador
# Create your models here.


class Vehiculo(models.Model):

    vehiculo = models.CharField(max_length=150)
    modelo = models.PositiveIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True, max_length=200)
    precio_mercado = models.FloatField(
        blank=True, null=True, verbose_name='Precio de Mercado')
    stock = models.BooleanField()

    def __str__(self):
        return self.vehiculo


class Operacion (models.Model):

    fecha = models.DateField()
    operacion = models.CharField(max_length=10, choices=[
                                 ('Compra', 'Compra'),
                                 ('Venta', 'Venta')
                                 ])
    responsable = models.ForeignKey(
        Cobrador, on_delete=models.PROTECT, default=1)
    monto = models.FloatField()
    descripcion = models.TextField(max_length=200)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, default=1)

from django.db import models
from apps.pago.models import Cobrador
# Create your models here.


class Activo(models.Model):
    # Dolar, USDT, Euro, Real, etc.
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class OperacionCambio(models.Model):
    fecha = models.DateField()
    operador = models.ForeignKey(Cobrador, on_delete=models.PROTECT)
    activo = models.ForeignKey(Activo, on_delete=models.PROTECT, default=1)
    operacion = models.CharField(max_length=10, choices=[
                                 ('Compra', 'Compra'),
                                 ('Venta', 'Venta')
                                 ])
    cantidad = models.FloatField()
    comision = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    referencia = models.TextField(max_length=200)

    def __str__(self):
        return 'Operacion: ' + self.operacion + ' de ' + str(self.cantidad) + ' ' + self.activo.nombre

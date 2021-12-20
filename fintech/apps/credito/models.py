from django.db import models
from .managers import CreditoManager, CuotaManager
from apps.cliente.models import Cliente
# Create your models here.


class Mora(models.Model):
    descripcion = models.CharField(max_length=50)
    tasa = models.FloatField(default=0.15)

    def __str__(self):
        return self.descripcion


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
    tasa_interes = models.FloatField()
    cant_cuota = models.IntegerField()
    mora = models.ForeignKey(Mora, on_delete=models.PROTECT, default=1)
    monto_mora = models.FloatField(default=0)
    activo = models.BooleanField(default=True)
    situacion = models.CharField(max_length=20, choices=ESTADOS, default=OK)
    objects = CreditoManager()

    def __str__(self):
        return str(self.titular)

# Flujo de registro de cuota. Se crea el Titular del credito, luego se registra el credito
# Con sus respectivos valores. en ese momento se generan las cuotas de forma automatica
# Las cuotas perteneceraen al credito, por ej, pk=12312


class Cuota(models.Model):
    PAGADO = 'Pagado'
    # Cuota pendiente es aquella que no ha vencido.
    PENDIENTE = 'Pendiente'
    SIN_PAGO = 'No realizo Pago'
    # Cuota pago_parcial es aquella en donde el pago es inferior al monto de la cuota.
    PAGO_PARCIAL = 'Pago parcial'
    SITUACION = (
        (PAGADO, 'Pagado'),
        (PENDIENTE, 'Pendiente de Pago'),
        (PAGO_PARCIAL, 'Pago Parcial'),
        (SIN_PAGO, 'No realizo Pago'),

    )
    situacion = models.CharField(
        max_length=30, choices=SITUACION, default=PENDIENTE)
    capital_amortizable = models.FloatField()
    amortizacion = models.FloatField(default=0)
    interes = models.FloatField()
    numero_cuota = models.PositiveIntegerField()
    monto_cuota = models.FloatField()
    mora_cuota = models.FloatField(default=0)
    fecha_pago = models.DateField()
    credito = models.ForeignKey(Credito, on_delete=models.PROTECT)
    objects = CuotaManager()

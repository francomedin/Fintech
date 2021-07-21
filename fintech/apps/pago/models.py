from apps.credito.models import Credito
from django.db import models

# Create your models here.


class Pago(models.Model):

    monto = models.FloatField()
    fecha = models.DateField()
    monto = models.FloatField()
    credito = models.ForeignKey(Credito, on_delete=models.PROTECT, default=1)

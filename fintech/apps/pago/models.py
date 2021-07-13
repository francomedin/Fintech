from django.db import models

# Create your models here.


class Pago(models.Model):
    monto = models.FloatField()
    fecha = models.DateTimeField()
    # credito=
    # cliente=

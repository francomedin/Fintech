from django.db import models

# Create your models here.


class Cuenta(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Registro(models.Model):
    fecha = models.DateField()
    monto = models.FloatField(default=0)
    cuentas = models.ManyToManyField(Cuenta)

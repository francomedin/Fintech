from django.db import models


class Cliente(models.Model):

    ACTIVO = 'Activo'
    # Actualmente no tiene creditos activos(tuvo pero los termino)
    INACTIVO = 'No Tuvo credito'
    LIBRE = 'Sin Credito'
    JUICIO = 'En Juicio'
    SITUACION = (
        (ACTIVO, 'Con Credito Activo'),
        (LIBRE, 'Con Credito/s Finalizados'),
        (JUICIO, 'En Gestion Judicial'),
        (INACTIVO, 'Sin registro de creditos'),

    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=20)
    cbu = models.CharField(max_length=30)
    ocupacion = models.CharField(max_length=20)
    direccion = models.CharField(max_length=70)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)
    situacion = models.CharField(
        max_length=15, choices=SITUACION, default=ACTIVO)

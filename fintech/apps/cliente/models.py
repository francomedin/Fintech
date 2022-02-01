from django.db import models
from django.urls import reverse


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
    BCRA = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),

    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    direccion = models.CharField(max_length=70)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)

    cbu = models.CharField(max_length=30)
    tipo_empleo = models.CharField(max_length=20, choices=(
        ('Publico', 'Publico'),
        ('Privado', 'Privado')
    ),
        default='Publico')
    ocupacion = models.CharField(max_length=30)
    sueldo_bruto = models.FloatField(default=0)
    situacion = models.CharField(
        max_length=15, choices=SITUACION, default=ACTIVO)
    bcra = models.CharField(
        max_length=20, choices=BCRA, default=1
    )
    
    activo = models.BooleanField(default=True)
    embargo = models.BooleanField(default=False)
    juicios = models.TextField(default='Sin juicios')

    observacion = models.TextField(default='')

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

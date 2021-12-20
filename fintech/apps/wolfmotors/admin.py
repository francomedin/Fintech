from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from apps.wolfmotors.models import Vehiculo, Operacion

# Register your models here.


class OperacionResource(resources.ModelResource):

    class Meta:
        model = Operacion
        fields = (
            'fecha',
            'operacion',
            'responsable__nombre',
            'monto',
            'vehiculo',
            'id',
        )


class OperacionAdmin(ImportExportModelAdmin):
    resorce_class = OperacionResource
    list_display = ('fecha', 'operacion', 'monto', 'vehiculo')


class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'modelo', 'precio_mercado')


admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Operacion, OperacionAdmin)

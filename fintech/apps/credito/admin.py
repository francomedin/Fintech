from django.contrib import admin
from .models import Credito, Mora, Cuota
# Register your models here.


class MoraAdmin(admin.ModelAdmin):
    list_display = ('descripcion_mora', 'monto_mora')


class CreditoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'titular')


class CuotaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'credito', 'situacion')


admin.site.register(Credito, CreditoAdmin)
admin.site.register(Mora, MoraAdmin)
admin.site.register(Cuota, CuotaAdmin)

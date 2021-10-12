from django.contrib import admin
from .models import Pago, Cobrador, TipoPago, MetodoPago
# Register your models here.


class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('metodo_pago')


admin.site.register(Pago)
admin.site.register(Cobrador)
admin.site.register(TipoPago)
admin.site.register(MetodoPago)

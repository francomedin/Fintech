from django.contrib import admin
from .models import Credito, Mora, Cuota
# Register your models here.


class MoraAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'tasa')


class CreditoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'titular')


admin.site.register(Credito,CreditoAdmin)
admin.site.register(Mora, MoraAdmin)
admin.site.register(Cuota)

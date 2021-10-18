from django.contrib import admin
from .models import Credito, Mora, Cuota
# Register your models here.


class MoraAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'tasa')


admin.site.register(Credito)
admin.site.register(Mora, MoraAdmin)
admin.site.register(Cuota)

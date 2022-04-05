from django import template
from apps.credito.models import Cuota,Mora
register = template.Library()

@register.simple_tag
def adeudado(cuota):
    cuota=Cuota.objects.get(pk=cuota)
    try:
        mora_obj=Mora.objects.get(cuota=cuota)
        mora=mora_obj.monto_mora
    except:
        mora=0 
    total_adeudado=(cuota.monto_cuota + mora) - cuota.total_pagado
    if total_adeudado<0:
        total_adeudado=0
    
    return round(total_adeudado)
register.filter('adeudado', adeudado)
   

@register.simple_tag
def redondear(numero):
    return round(numero)
register.filter('redondear', redondear)



@register.simple_tag
def pagado(cuota):
    cuota=Cuota.objects.get(pk=cuota)
    try:
        mora_obj=Mora.objects.get(cuota=cuota)
        mora=mora_obj.monto_mora
    except:
        mora=0 
    total_adeudado=(cuota.monto_cuota + mora) - cuota.total_pagado
    if total_adeudado<0:
        total_adeudado=0
    
    return round(total_adeudado)
register.filter('adeudado', adeudado)
from django.db import models
from apps.credito.managers import CuotaManager
from apps.credito.models import Cuota, Credito,Mora

from datetime import datetime
import calendar


class PagoManager(models.Manager):

    def cargar_pago(self, cuota, monto, fecha, descripcion, tipo, metodo, cobrador):

        self.create(
            cuota=cuota,
            monto=monto,
            fecha=fecha,
            descripcion=descripcion,
            tipo=tipo,
            metodo=metodo,
            cobrador=cobrador

        )
        #Cargo el $ total de pagos realizado para dicha cuota
        self.total_pagado(cuota)
        self.set_situacion(cuota)

        
        
        #Cambio la situación de la cuota
        """Si el total pagado es < al total adeudado.
        El total adeudado es monto_cuota + mora_cuota
        """

        # Al cargar un pago quiere que:
        # Cambiar situacion.
        #self.set_situacion(cuota, monto)
        # Envie el saldo de las cuotas no pagadas a Mora.
        # self.cargar_saldos_morosos()
        
    def total_pagado(self,cuota):
        todos_pagos=self.filter(cuota__pk=cuota.pk)
        total_pagos=0
        for pago in todos_pagos:
            total_pagos+=pago.monto
       
        Cuota.objects.total_pagado(cuota,total_pagos)

    def set_situacion(self, cuota, monto_pagado):
        today = datetime.now()

        self.set_no_pagadas(today)
        self.set_pagadas(cuota, monto_pagado)

        """Actualizar situacion de cuotas pendites a: pagadas, pago parcial y no pagadas."""

    def set_situacion(self, cuota):
        hoy=datetime.now()
        print(hoy)
        pk=cuota.pk
        mora=Mora.objects.get_mora(cuota.pk)
        total_adeudado=cuota.monto_cuota+ mora
        print(total_adeudado,'total adeudado')
        total_pagado=cuota.total_pagado
        print(total_pagado,'total pagado')


        if total_pagado>=total_adeudado:
            cuota.situacion='Pagado'
        elif total_pagado<total_adeudado:
            cuota.situacion='Pago Parcial'
        elif (total_pagado==0 or total_pagado=='') and cuota.fecha_pago > hoy:
            cuota.situacion='No Pago'
        else:
            cuota.situacion='Pendiente'
        cuota.save()
        print(cuota.situacion)


        

    

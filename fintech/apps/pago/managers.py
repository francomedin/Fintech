from django.db import models
from apps.credito.managers import CuotaManager
from apps.credito.models import Cuota, Credito

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
        # Al cargar un pago quiere que:
        # Cambiar situacion.
        self.set_situacion(cuota, monto)
        # Envie el saldo de las cuotas no pagadas a Mora.
        # self.cargar_saldos_morosos()

    def set_situacion(self, cuota, monto_pagado):
        today = datetime.now()

        self.set_no_pagadas(today)
        self.set_pagadas(cuota, monto_pagado)

        """Actualizar situacion de cuotas pendites a: pagadas, pago parcial y no pagadas."""

    def set_pagadas(self, cuota, monto_pagado):

        total_pagado = 0
        pagos = self.filter(cuota=cuota, monto__gte=0)

        # Verifico si hay pagos previos, incluye el pago que estoy cargando.
        if len(pagos) > 1:
            for pago in pagos:
                total_pagado += pago.monto

            if cuota.mora_cuota > 0:
                if total_pagado >= cuota.mora_cuota:

                    cuota.situacion = 'Pagado'
                    cuota.mora_cuota = 0
                    cuota.total_pagado = total_pagado

                # La suma de los pagos es menor a la mora.
                else:
                    cuota.situacion = 'Pago Parcial'
                    cuota.mora_cuota -= total_pagado
                    cuota.total_pagado = total_pagado
            # Hay mas de un pago y no hay mora.
            else:
                # Paga el total
                if total_pagado >= cuota.monto_cuota:
                    cuota.situacion = 'Pagado'
                    cuota.mora_cuota = 0
                    cuota.total_pagado = total_pagado
                # Paga una parte.
                else:
                    cuota.situacion = 'Pago Parcial'
                    cuota.mora_cuota = cuota.monto_cuota - total_pagado
                    cuota.total_pagado = total_pagado

        # No hay pagos anteriores
        else:
            total_pagado = monto_pagado
            # No tengo mora
            if cuota.mora_cuota <= 0:
                # No tengo mora y pago total
                if total_pagado >= cuota.monto_cuota:
                    cuota.situacion = 'Pagado'
                    cuota.mora_cuota = 0
                    cuota.total_pagado = total_pagado

                # No tengo mora y pago parcial
                else:
                    cuota.situacion = 'Pago Parcial'
                    cuota.mora_cuota = cuota.monto_cuota - total_pagado
                    cuota.total_pagado = total_pagado

            # Tengo mora, primer pago y paga parcial: Situacion que se da cuando la cuota se atrasa
            # y no efectua pago alguno.
            elif cuota.situacion == 'No realizo Pago':
                if total_pagado < cuota.mora_cuota:
                    cuota.situacion = 'Pago Parcial'
                    cuota.mora_cuota -= total_pagado
                    cuota.total_pagado = total_pagado

            # Tengo mora y paga el saldo total:
                else:
                    cuota.situacion = 'Pagado'
                    cuota.mora_cuota = 0
                    cuota.total_pagado = total_pagado

        cuota.save()

    def set_no_pagadas(self, today):
        # Si el dia de la fecha es mayor que 10 actualiza
        # situaciones "No pagadas"

        if today.day > 2:

            cuotas = []
            # Devuelve una tupa con el inicio y final del mes.
            month_range = calendar.monthrange(today.year, today.month)

            # Obtengo las cuotas pendientes de pagos del mes
            cuotas = Cuota.objects.filter(
                fecha_pago__gte=f"{today.year}-{today.month}-{month_range[0]}",
                fecha_pago__lte=f"{today.year}-{today.month}-{month_range[1]}",
                situacion='Pendiente'
            )

            for cuota in cuotas:
                cuota.situacion = 'No realizo Pago'
                cuota.mora_cuota = cuota.monto_cuota
                cuota.save()

   

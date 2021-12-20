from django.db import models
from apps.credito.managers import CuotaManager
from apps.credito.models import Cuota, Credito


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

    def set_situacion(self, cuota, monto, fecha):

        credito = Credito.objects.filter(pk=cuota.credito.pk)
        situacion = ''
        saldo_mora = 0 + credito.monto_mora

        # Paga a fecha
        if cuota.fecha_pago >= fecha:

            # Paga y se queda al dia
            if cuota.monto_cuota + saldo_mora == monto:
                situacion = 'Pagado'
                saldo_mora = 0
                credito.monto_mora = 0
            # El monto abonado difere del saldo adeudado
            else:
                # Pago de mas
                if cuota.monto_cuota + saldo_mora < monto:
                    situacion = 'Pagado'
                    saldo_mora = 0
                    # actualizo el saldo mora en el credito
                    credito.monto_mora = 0

                # Pago menos que el total adeudado
                elif cuota.monto_cuota + saldo_mora > monto and monto > 0:
                    situacion = 'Pago parcial'
                    # actualizo la mora DE LA CUOTA.
                    # Si la mora = 0 va a ser el monto de cuota - lo pagado
                    if saldo_mora == 0:
                        saldo_mora = cuota.monto_cuota - monto

                    # En caso de que ya haya mora, el saldo pendiente sera
                    # saldo_mora-monto
                    else:
                        saldo_mora = saldo_mora-monto

                    credito.monto_mora += saldo_mora

                # No Realizo ningun pago.
                elif monto == 0:
                    situacion = 'No realizo Pago'
                    saldo_mora = cuota.monto_cuota1
                    credito.monto_mora += saldo_mora

        # Paga fuera de fecha
        else:
            print('hola')
            # Deberia calcular la mora hasta el dia
            # Imputar el pago a los saldos pendientes del credito
            # Imputar a la cuota del mes en curso.
            # Crear funcion que calcule la mora

    def calcular_mora(self, fecha_vencimiento, fecha_pago, tasa, saldo_adeudado):

        dias = fecha_vencimiento-fecha_pago
        tasa_diaria = round(tasa/30.4166, 2)
        mora_monto = dias*tasa_diaria*saldo_adeudado

        return mora_monto

        # Si entra en el if esta pagando atrasado
        if cuota.fecha_pago < fecha:

            if cuota.monto_cuota > monto:
                situacion = 'Pago parcial'
                saldo_mora = cuota.monto_-monto

            elif monto == 0:
                situacion = 'No realizo Pago'
                saldo_mora = cuota.monto_cuota

        elif cuota.fecha_pago >= fecha and cuota.monto_cuota == monto:
            situacion = 'Pagado'

        elif cuota.fecha_pago >= fecha and cuota.monto_cuota < monto:
            situacion = 'Pago parcial'
            saldo_mora = cuota.monto_-monto

        cuota.situacion = situacion
        cuota.mora_cuota = saldo_mora

        cuota.save()
        credito.save()
    # Calcular la mora todos los 10.
    # La mora se tratara de la siguiente forma:
    # Cuando se realice un pago menor a la cuota se cargara el atributo "mora cuota" con el saldo adeudado
    # Al dia 10 se cargaran los saldos en el atributo mora del credito.
    # Porque no actualziar el dai del pago y los dias 10?: Porque se va a capitalizar.

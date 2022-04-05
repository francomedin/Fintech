from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import datetime
#from apps.pago.models import Pago



# En caso de que la fecha se vea modificada va a ser necesario actualizar todas las cuotas.


class CuotaManager(models.Manager):

    def create_cuotas(self, credito_obj, capital, fecha, p_tasa_interes, cant_cuota):

        # Formulas:
        # ---> Cuota= capital*tasa_interes/1-(1+tasa_interes)**(-cant_cuota)
        # ---> Capital_remanente/A amortizar= capital - Amortizaciones
        # ---> Interes= Capital_remanente - tasa_interes
        # ---> Fecha de pago= Se toma como punto de corte el dia 15. Si el credito es posterior,
        # se abona el mes siguiente.

        # Procesamiento para calcular el valor de la cuota, sistema de amortizacion frances.
        numerador = capital*(p_tasa_interes)
        denominador = 1-((1+p_tasa_interes)**(-cant_cuota))
        valor_cuota = round(numerador/denominador, 2)

        # Tratamiento de la fecha

        dia = fecha.day
        mes = 0

        if dia > 15:
            mes += 2

        else:
            mes += 1

        # Se crean todas las cuotas que perteneceran al credito

        capital_remanente = capital

        for i in range(cant_cuota):
            interes_monto = round(capital_remanente * p_tasa_interes, 2)
            amortizacion = round(valor_cuota - interes_monto, 2)

            self.create(

                capital_amortizable=capital_remanente,
                interes=interes_monto,
                numero_cuota=(i) + 1,
                amortizacion=amortizacion,
                monto_cuota=valor_cuota,
                fecha_pago=fecha + relativedelta(day=10, months=i+mes),

                credito=credito_obj
            )

            capital_remanente = round(capital_remanente-amortizacion, 2)

    def total_pagado(self,cuota,sum_pagos):
        #Recibe la cuota y monto abonado. Acumula
       
        cuota.total_pagado=sum_pagos
        cuota.save()
       
    


class CreditoManager(models.Manager):

    # Este metodo recibe como parametro capital, interes y cant_cuotas, crea un objeto credito.
    def create_credito(self, titular, capital, fecha, p_tasa_interes, cant_cuota):

        numerador = capital*(p_tasa_interes)
        denominador = 1-((1+p_tasa_interes)**(-cant_cuota))
        valor_cuota = round(numerador/denominador, 2)

        credito_obj = self.create(
            titular=titular,
            capital=capital,
            fecha_prestamo=fecha,
            tasa_interes=p_tasa_interes * 100,
            cant_cuota=cant_cuota,
            monto_cuota=valor_cuota
        )
        return credito_obj


class MoraManager(models.Manager):

    def create_mora(self, cuota, monto, descripcion):
        self.create(

            cuota=cuota,
            monto_mora=monto,
            descripcion_mora=descripcion

        )
    
    def get_credito_pk(self,pk):
        mora=self.get(id=pk)
        credito=mora.cuota.credito.pk
      
    
        return credito
    
    def get_mora(self,cuota_pk):
        try:
            mora_obj=self.get(cuota=cuota_pk)
            mora=mora_obj.monto_mora
        except:
            mora=0
            
        return mora

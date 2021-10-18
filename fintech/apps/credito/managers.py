from django.db import models
from dateutil.relativedelta import relativedelta

# Aca vamos a calcular la cuota en base a la tasa de interes, cant_cuotas y monto.


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
            mes = 1

        # Se crean todas las cuotas que perteneceran al credito
        i = 1
        capital_remanente = capital

        for i in range(cant_cuota):

            interes_monto = round(capital_remanente * p_tasa_interes, 2)
            amortizacion = round(valor_cuota - interes_monto, 2)

            self.create(

                capital_amortizable=capital_remanente,
                interes=interes_monto,
                numero_cuota=i,
                amortizacion=amortizacion,
                monto_cuota=valor_cuota,
                fecha_pago=fecha + relativedelta(months=(i+mes)),
                credito=credito_obj

            )
            capital_remanente = round(capital_remanente-amortizacion, 2)


class CreditoManager(models.Manager):

    # Este metodo recibe como parametro capital, interes y cant_cuotas, crea un objeto credito.
    def create_credito(self, titular, capital, fecha, p_tasa_interes, cant_cuota):

        credito_obj = self.create(
            titular=titular,
            capital=capital,
            fecha_prestamo=fecha,
            tasa_interes=p_tasa_interes,
            cant_cuota=cant_cuota
        )
        return credito_obj
        # def update_mora():
        # Esto se me ocurre de 2 formas. Con un boton que se aprieta n dia del mes y calcula todas las moras

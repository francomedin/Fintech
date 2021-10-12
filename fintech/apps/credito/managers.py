from django.db import models

# Aca vamos a calcular la cuota en base a la tasa de interes, cant_cuotas y monto.


class CreditoManager(models.Manager):

    # Este metodo recibe como parametro capital, interes y cant_cuotas, crea un objeto credito.
    def create_credito(self, capital, fecha, interes, cant_cuota):

        # Procesamiento para calcular el valor de la cuota, sistema de amortizacion frances.
        cuota = 0
        numerador = capital*interes
        denominador = 1-((1+interes)**(-cant_cuota))
        cuota = round(numerador/denominador, 2)

        self.create(capital=capital,
                    fecha_prestamo=fecha,
                    tasa_interes=interes,
                    cant_cuota=cant_cuota,
                    monto_cuota=cuota)

    # def update_mora():
    # Esto se me ocurre de 2 formas. Con un boton que se aprieta n dia del mes y calcula todas las moras

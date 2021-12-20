from django import forms
from apps.pago.models import Pago


class PagoForm(forms.ModelForm):

    class Meta:

        model = Pago
        fields = ('cuota', 'monto', 'fecha',
                  'descripcion', 'tipo', 'metodo', 'cobrador')

    monto = forms.FloatField(
        label='Capital',
        required=True)
    monto.widget.attrs.update({'placeholder': 'Ingrese el capital'})

    fecha = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    descripcion = forms.CharField()

    descripcion.widget.attrs.update(
        {'placeholder': 'Ingresar descripcion mensual',
            'label': 'Tasa de Interes (Numero entero)'}

    )

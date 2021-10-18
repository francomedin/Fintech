
from django import forms
from apps.credito.models import Credito
from django.contrib.admin.widgets import AdminDateWidget


class CreditoForm(forms.ModelForm):

    class Meta:

        model = Credito
        fields = ('titular', 'capital', 'fecha_prestamo',
                  'tasa_interes', 'cant_cuota')

    capital = forms.FloatField(
        label='Capital',
        required=True)
    capital.widget.attrs.update({'placeholder': 'Ingrese el capital'})

    fecha_prestamo = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    tasa_interes = forms.FloatField(
        label='Tasa de Interes (Numero entero)',
        required=True)
    tasa_interes.widget.attrs.update(
        {'placeholder': 'Ingresar Interes mensual'})

    cant_cuota = forms.IntegerField(
        label='Cantidad de Cuotas',
        required=True)
    cant_cuota.widget.attrs.update(
        {'placeholder': 'Cantidad de Cuotas'})

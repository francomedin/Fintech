
from django import forms
from apps.credito.models import Credito, Cuota, Mora
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


class CreditoPkForm(forms.ModelForm):

    class Meta:

        model = Credito
        fields = ('capital', 'fecha_prestamo',
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


class MoraFormPk(forms.ModelForm):
    class Meta:

        model = Mora
        fields = (

            'monto_mora',
            'descripcion_mora',
            'cargador_mora'
        )

    monto_mora = forms.FloatField(
        label='Monto de Mora',
        required=True)
    monto_mora.widget.attrs.update({'placeholder': 'Ingrese la Mora'})

    descripcion_mora = forms.CharField(
        label='Descripcion',
        required=False)
    descripcion_mora.widget.attrs.update(
        {'placeholder': 'Descripcion'})

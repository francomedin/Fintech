from django import forms
from .models import Cliente
from datetime import datetime


class ClienteForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Cliente
        fields = ('nombres', 'apellidos', 'dni', 'telefono', 'cbu', 'ocupacion','tipo_empleo', 'direccion',
                  'fecha_nacimiento', 'activo','bcra', 'situacion', 'juicios', 'observacion')

      
        
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'cbu': forms.NumberInput(attrs={'class': 'form-control'}),
            #'tipo_empleo': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(1950, (datetime.now().year-17))),
            #'activo': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            #'bcra': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'situacion': forms.RadioSelect(attrs={'class': 'form-control'}),
            'juicios': forms.Textarea(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'})



        }

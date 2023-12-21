# forms.py

from django import forms
from .models import Boleto
from BusesApp.models import Bus
from PasajerosApp.models import Pasajero

class BoletoForm(forms.ModelForm):
    class Meta:
        model = Boleto
        fields = ['Precio', 'Hora_Viaje', 'Fecha_Viaje', 'Origen', 'Destino', 'Numero_de_Asiento']
        widgets = {
            'bus': forms.Select(attrs={'class': 'form-control'}),
            'pasajero': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personalizar las opciones del campo 'bus'
        self.fields['bus'] = forms.ModelChoiceField(
            queryset=Bus.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            label='Seleccionar Bus',
            to_field_name='id',
            empty_label=None,
            initial=None,
        )

        self.fields['bus'].label_from_instance = lambda obj: f"{obj.Matricula} - {obj.Tipo_de_bus} - {obj.Empresa}"

        # Personalizar las opciones del campo 'pasajero'
        self.fields['pasajero'] = forms.ModelChoiceField(
            queryset=Pasajero.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            label='Seleccionar Pasajero',
            to_field_name='id',
            empty_label=None,
            initial=None,
        )

        self.fields['pasajero'].label_from_instance = lambda obj: f"{obj.nombre} - {obj.rut} - {obj.tipoPasajero}"


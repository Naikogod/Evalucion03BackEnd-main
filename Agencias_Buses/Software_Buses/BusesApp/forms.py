from django import forms
from .models import Bus
from django.core.exceptions import ValidationError

def validate_nombre_chofer(value):
    if not value:
        raise ValidationError('El campo Nombre Chofer no puede estar vacío.')

def validate_numero_de_asientos(value):
    if not value or not value.isnumeric():
        raise ValidationError('El número de asientos debe ser un número entero mayor que cero.')

def validate_matricula(value):
    if not value:
        raise ValidationError('El campo Matrícula no puede estar vacío.')

def validate_ano(value):
    if not value or not value.isnumeric():
        raise ValidationError('Ingrese el año en numeros.')

def validate_marca(value):
    if not value:
        raise ValidationError('El campo Marca no puede estar vacío.')

def validate_tipo_de_bus(value):
    if not value:
        raise ValidationError('Seleccione el tipo de bus.')

def validate_empresa(value):
    if not value:
        raise ValidationError('El campo Empresa no puede estar vacío.')

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'

    Nombre_Chofer = forms.CharField(validators=[validate_nombre_chofer])
    Numero_de_Asientos = forms.CharField(validators=[validate_numero_de_asientos])
    Matricula = forms.CharField(validators=[validate_matricula])
    Año = forms.CharField(validators=[validate_ano])
    Marca = forms.CharField(validators=[validate_marca])
    Tipo_de_bus = forms.ChoiceField(choices=[('Dos Pisos', 'Dos Pisos'), ('Un Piso', 'Un Piso')], validators=[validate_tipo_de_bus])
    Empresa = forms.CharField(validators=[validate_empresa])

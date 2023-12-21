from rest_framework import serializers
from BusesApp.models import Bus
from PasajerosApp.models import Pasajero
from BoletosApp.models import Boleto

class ListaBusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class ListaPasajerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'

class ListaBoletosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleto
        exclude = ['matricula', 'tipo_de_bus', 'empresa', 'nombre', 'rut', 'tipoPasajero']
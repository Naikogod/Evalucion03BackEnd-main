from django.db import models
from BusesApp.models import Bus
from PasajerosApp.models import Pasajero

# Create your models here.

class Boleto(models.Model):
    Precio = models.DecimalField(max_digits=8, decimal_places=2)
    Hora_Viaje = models.TimeField()
    Fecha_Viaje = models.DateField()
    Destino = models.CharField(max_length=100)
    Origen = models.CharField(max_length=100)
    Numero_de_Asiento = models.PositiveIntegerField()

    # Relación con la app BusesApp
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

    # Herencia de atributos de Bus
    matricula = models.CharField(max_length=20)
    tipo_de_bus = models.CharField(max_length=10, choices=[('Dos Pisos', 'Dos Pisos'), ('Un Piso', 'Un Piso')])
    empresa = models.CharField(max_length=100)

    # Relación con la app PasajerosApp
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)

    # Herencia de atributos de Pasajero
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    tipoPasajero = models.CharField(max_length=20, choices=[
        ('Estudiante', 'Estudiante'),
        ('AdultoMayor', 'Adulto Mayor'),
        ('Frecuente', 'Frecuente'),
        ('Normal', 'Normal'),
    ])

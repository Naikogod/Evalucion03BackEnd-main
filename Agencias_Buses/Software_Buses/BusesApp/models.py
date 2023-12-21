from django.db import models

# Create your models here.
class Bus(models.Model):
    Nombre_Chofer = models.CharField(max_length=100)
    Numero_de_Asientos = models.PositiveIntegerField()
    Matricula = models.CharField(max_length=20)
    Año = models.PositiveIntegerField()
    Marca = models.CharField(max_length=50)
    Tipo_de_bus = models.CharField(
        max_length=10,
        choices=[('Dos Pisos', 'Dos Pisos'), ('Un Piso', 'Un Piso')]
    )
    Empresa = models.CharField(max_length=100)

    def __str__(self):

        return f"{self.Matricula} - {self.Tipo_de_bus} - {self.Empresa}"
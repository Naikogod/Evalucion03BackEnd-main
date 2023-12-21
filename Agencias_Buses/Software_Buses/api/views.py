from rest_framework import generics
from BusesApp.models import Bus
from PasajerosApp.models import Pasajero
from BoletosApp.models import Boleto
from .serializers import ListaBusesSerializer, ListaPasajerosSerializer, ListaBoletosSerializer

class ListaBuses(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = ListaBusesSerializer

class DetalleBus(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = ListaBusesSerializer

class ListaPasajeros(generics.ListCreateAPIView):
    queryset = Pasajero.objects.all()
    serializer_class = ListaPasajerosSerializer

class DetallePasajero(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pasajero.objects.all()
    serializer_class = ListaPasajerosSerializer

class ListaBoletos(generics.ListCreateAPIView):
    queryset = Boleto.objects.all()
    serializer_class = ListaBoletosSerializer

class DetalleBoleto(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boleto.objects.all()
    serializer_class = ListaBoletosSerializer

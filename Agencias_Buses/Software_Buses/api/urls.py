from django.urls import path
from .views import ListaBuses, DetalleBus, ListaPasajeros, DetallePasajero, ListaBoletos, DetalleBoleto

urlpatterns = [
    path('buses/', ListaBuses.as_view(), name='bus-list-create'),
    path('buses/<int:pk>/', DetalleBus.as_view(), name='bus-retrieve-update-destroy'),
    path('pasajeros/', ListaPasajeros.as_view(), name='pasajero-list-create'),
    path('pasajeros/<int:pk>/', DetallePasajero.as_view(), name='pasajero-retrieve-update-destroy'),
    path('boletos/', ListaBoletos.as_view(), name='boleto-list-create'),
    path('boletos/<int:pk>/', DetalleBoleto.as_view(), name='boleto-retrieve-update-destroy'),
]


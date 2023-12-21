"""
URL configuration for Software_Buses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PasajerosApp import views as PasajerosApp
from BusesApp import views as BusesApp
from BoletosApp import views as BoletosApp


urlpatterns = [
    path('admin/', admin.site.urls),
    #Index
    path('', PasajerosApp.index),
    #Buses URL
    path('registrar/', BusesApp.registrar_bus, name='registrar_bus'),
    path('modificar/<int:bus_id>/', BusesApp.modificar_bus, name='modificar_bus'),
    path('eliminar/<int:bus_id>/', BusesApp.eliminar_bus, name='eliminar_bus'),
    path('mostrar/', BusesApp.listar_buses, name='mostrar_buses'),
    #Pasajeros Url
    path('pasajeros/', PasajerosApp.listadoPasajeros),
    path('agregarPasajero/', PasajerosApp.agregarPasajero),
    path('eliminarPasajero/<int:id>', PasajerosApp.eliminarPasajero),
    path('actualizarPasajero/<int:id>', PasajerosApp.actualizarPasajero),
    #Boletos URL
    path('Registrar_Boletos/', BoletosApp.AgregarBoletos, name= 'agregar_boleto'),
    path('Mostrar_Boletos', BoletosApp.ListadoBoletos),
    path('Actualizar_Boletos/<int:id>', BoletosApp.ActualizarBoletos), #No carga Template Propio/ redirigen a Mostrar
    path('Eliminar_Boletos/<int:id>', BoletosApp.EliminarBoletos), #No carga Template Propio/ redirigen a Mostrar
]

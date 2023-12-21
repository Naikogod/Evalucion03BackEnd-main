from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bus
from .forms import BusForm

#https://docs.djangoproject.com/en/4.2/ref/forms/validation/ Documentacion de las validaciones#

# Create your views here.
def listar_buses(request):
    buses = Bus.objects.all()
    return render(request, 'templatesBusesApp/listar_buses.html', {'buses': buses})

def registrar_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_buses')
    else:
        form = BusForm()
    return render(request, 'templatesBusesApp/registrar_bus.html', {'form': form})

def modificar_bus(request, bus_id):
    bus = Bus.objects.get(pk=bus_id)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('mostrar_buses')
    else:
        form = BusForm(instance=bus)
    return render(request, 'templatesBusesApp/modificar_bus.html', {'form': form, 'bus': bus})

def eliminar_bus(request, bus_id):
    bus = Bus.objects.get(pk=bus_id)
    if request.method == 'POST':
        bus.delete()
        return redirect('mostrar_buses')
    return render(request, 'templatesBusesApp/eliminar_bus.html', {'bus': bus})
from django.shortcuts import render, redirect
from BoletosApp.models import Boleto
from BoletosApp.forms import BoletoForm
from PasajerosApp.models import Pasajero
from BusesApp.models import Bus

# Create your views here.

def ListadoBoletos(request):
    boletos = Boleto.objects.all()
    data = {'boletos': boletos}  # Corregido de 'boleto' a 'boletos'
    for boleto in boletos:
        print(f"Matricula: {boleto.bus.Matricula}, Tipo de Bus: {boleto.bus.Tipo_de_bus}, Empresa: {boleto.bus.Empresa}")
        print(f"Nombre: {boleto.pasajero.nombre}, Rut: {boleto.pasajero.rut}, Tipo de Pasajero: {boleto.pasajero.tipoPasajero}")
    return render(request, 'templatesBoletosApp/mostrar_boletos.html', data)

def AgregarBoletos(request):
    if request.method == 'POST':
        form = BoletoForm(request.POST)
        if form.is_valid():
            # Obtener el objeto bus y pasajero seleccionados
            selected_bus = form.cleaned_data['bus']
            selected_pasajero = form.cleaned_data['pasajero']

            # Guardar el boleto en la base de datos con los detalles del bus y pasajero
            nuevo_boleto = Boleto(
                Precio=form.cleaned_data['Precio'],
                Hora_Viaje=form.cleaned_data['Hora_Viaje'],
                Fecha_Viaje=form.cleaned_data['Fecha_Viaje'],
                Origen=form.cleaned_data['Origen'],
                Destino=form.cleaned_data['Destino'],
                Numero_de_Asiento=form.cleaned_data['Numero_de_Asiento'],
                bus=selected_bus,
                pasajero=selected_pasajero,
                matricula=selected_bus.Matricula,
                tipo_de_bus=selected_bus.Tipo_de_bus,
                empresa=selected_bus.Empresa,
                nombre=selected_pasajero.nombre,
                rut=selected_pasajero.rut,
                tipoPasajero=selected_pasajero.tipoPasajero,
            )
            nuevo_boleto.save()
            return redirect('/Mostrar_Boletos')
    else:
        form = BoletoForm()

    data = {'form': form}
    return render(request, 'templatesBoletosApp/agregar_boletos.html', data)

def EliminarBoletos(request, id):
    boletos = Boleto.objects.get(id = id)
    boletos.delete()
    return redirect('/Mostrar_Boletos')

def ActualizarBoletos(request, id):
    boleto = Boleto.objects.get(id=id)
    if request.method == 'POST':
        form = BoletoForm(request.POST, instance=boleto)
        if form.is_valid():
            # Obtener los objetos de bus y pasajero seleccionados
            selected_bus = form.cleaned_data['bus']
            selected_pasajero = form.cleaned_data['pasajero']

            # Actualizar los campos de boleto
            form.instance.Precio = form.cleaned_data['Precio']
            form.instance.Hora_Viaje = form.cleaned_data['Hora_Viaje']
            form.instance.Fecha_Viaje = form.cleaned_data['Fecha_Viaje']
            form.instance.Origen = form.cleaned_data['Origen']
            form.instance.Destino = form.cleaned_data['Destino']
            form.instance.Numero_de_Asiento = form.cleaned_data['Numero_de_Asiento']

            # Actualizar los campos personalizados de bus y pasajero
            form.instance.bus = selected_bus
            form.instance.pasajero = selected_pasajero
            form.instance.matricula = selected_bus.Matricula
            form.instance.tipo_de_bus = selected_bus.Tipo_de_bus
            form.instance.empresa = selected_bus.Empresa
            form.instance.nombre = selected_pasajero.nombre
            form.instance.rut = selected_pasajero.rut
            form.instance.tipoPasajero = selected_pasajero.tipoPasajero

            # Guardar el objeto actualizado
            form.save()

            return redirect('/Mostrar_Boletos')

    else:
        form = BoletoForm(instance=boleto)

    data = {'form': form, 'boleto': boleto}
    return render(request, 'templatesBoletosApp/agregar_boletos.html', data)


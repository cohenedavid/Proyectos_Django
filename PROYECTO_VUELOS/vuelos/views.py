from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import request
from vuelos.models import Vuelo, Pasajero

# Create your views here.
def index(request):
    return render(request, 'vuelos/index.html',
        {"vuelos": Vuelo.objects.all()})

def vuelo(request, id_vuelo):
    vuelo= Vuelo.objects.get(id= id_vuelo)
    pasajeros= vuelo.pasajeros.all()
    noPasajeros=  Pasajero.objects.exclude(vuelos= vuelo).all()
    return render(request, 'vuelos/vuelo.html', 
        {'vuelo': vuelo,
        'pasajeros': pasajeros,
        'noPasajeros': noPasajeros}
        )

def reserva(request, id_vuelo):
    if request.method == "POST":
        vuelo= Vuelo.objects.get(pk= id_vuelo)
        id_pasajero= int(request.POST["pasajero"])
        pasajero= Pasajero.objects.get(pk= id_pasajero)
        pasajero.vuelos.add(vuelo)
        return HttpResponseRedirect(reverse('vuelos:vuelo', args=[id_vuelo]))

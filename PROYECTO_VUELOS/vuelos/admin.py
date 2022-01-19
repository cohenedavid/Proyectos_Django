from django.contrib import admin
from .models import Vuelo, Aeropuerto, Pasajero


class VueloAdmin(admin.ModelAdmin):
    list_display= ('id', 'origen', 'destino', 'duracion')

"""class PasajeroAdmin(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'apellido')"""
    
# Register your models here.
admin.site.register(Vuelo, VueloAdmin)
admin.site.register(Aeropuerto)
admin.site.register(Pasajero) # (Pasajero, PasajeroAdmin)
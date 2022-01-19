from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
#tareas=["despertarme","ordenar el cuarto","barrer el piso","ir a la tienda"]

def index(request):
    if "tareas" not in request.session:             # CHEAQUEA SI LA VARIALBLE TAREA ESTA CREADA EN MI SESION
        request.session["tareas"] = []              # SI NO EXISTE, CREA UNA NUEVA LISTA  "tareas" VACIA
    return render(request, "tareas/index.html",
                {"tareas":request.session["tareas"]})

# AGREGAR UNA NUEVA TAREA
def agregar(request):
    if request.method == "POST":                    # CHEQUEA QUE EL METODO SEA "POST"
        form= formNuevaTarea(request.POST)
        if form.is_valid():                         # CHEQUEA DEL LADO DEL SERVIDOR LA VALIDEZ DE LOS DATOS
            tarea= form.cleaned_data["tarea"]       # HACE LOS CONTROLES PARA PURGAR ESA INFORMACION
            request.session["tareas"] += [tarea] 
            return HttpResponseRedirect(reverse("tareas:index")) # REDIRECCIONA AL USUARIO A LA LISTA DE TAREAS
        else:
            return render(request, "tareas/agregar.html",
                    {"form": form})                 # SI EL FORMULARIO ES INVALIDO RENDERIZA LA PAGINA CON LOS DATOS QUE YA TENEMOS

    return render(request, "tareas/agregar.html",
                {"form": formNuevaTarea()})         # RECIBE UN FORMULARIO 


class formNuevaTarea(forms.Form):
    tarea= forms.CharField(label= "Nombre de la tarea")
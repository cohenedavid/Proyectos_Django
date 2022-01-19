from django.urls import path
from . import views

app_name= "tareas"
urlpatterns = [
    path("", views.index, name="index"),
    path("agregar", views.agregar, name="agregar"),
]

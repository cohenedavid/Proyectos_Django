from django.urls import path, include
from . import views

app_name= 'vuelos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_vuelo>', views.vuelo, name='vuelo'),
    path('<int:id_vuelo>/reserva', views.reserva, name='reserva'),
]

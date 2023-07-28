from django.urls import path, include
from.views import *

urlpatterns = [
    path('', index, name = "inicio"),
    path('monitor', monitor, name = "monitor"),
    path('placaDeVideo', placa_devideo, name = "placaDeVideo"),
    path('procesador', procesador, name = "procesador"),
    path('usuario', usuario, name = "usuario"),
    

]
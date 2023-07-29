from django.urls import path, include
from.views import *

urlpatterns = [
    path('', index, name = "inicio"),

    path('monitor/', monitor, name = "monitor"),
    path('placaDeVideo/', placa_devideo, name = "placaDeVideo"),
    path('procesador/', procesador, name = "procesador"),
    path('usuario/', usuarios, name = "usuario"),

# urls de FORMS
    path('monitor_form/', monitorForm, name = "monitor_form"),
    path('placaDeVideo_form/', PlacaDeVideoForm, name = "placaDeVideo_form"),
    path('procesador_form/', procesadorForm, name = "procesador_form"),
    path('usuario_form/', usuarioForm, name = "usuario_form"),


# urls de busqueda
  path('buscar_monitor/', buscarmonitor, name = "buscar_monitor"),
  path('buscar2/', buscar2, name = "buscar2"),





    

]
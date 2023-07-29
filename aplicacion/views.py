from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from.forms import *

# Create your views here.

def index(request):
    return render(request,"aplicacion/base.html")

def procesador(request):
    ctx = {"procesador": Procesador.objects.all() }
    return render(request,"aplicacion/procesador.html", ctx)

def placa_devideo(request):
    ctx = {"placadevideo": placaDeVideo.objects.all() }
    return render(request,"aplicacion/placadevideo.html", ctx)

def monitor(request):
    ctx = {"monitor": Monitor.objects.all() }
    return render(request,"aplicacion/monitor.html", ctx)

def usuarios(request):
    ctx = {"usuarios": usuario.objects.all() }
    return render(request,"aplicacion/usuario.html", ctx)


# Funcion FORM


def monitorForm(request):
    if request.method == "POST":
       miForm = MonitorForm(request.POST)
       if miForm.is_valid():
           informacion = miForm.cleaned_data
           monitr = Monitor(marca = informacion['marca'], modelo = informacion['modelo'], tamaño = informacion['tamaño'])
           monitr.save()
           return render(request, "aplicacion/base.html")
    else:
       miForm = MonitorForm()

    return render(request, "aplicacion/monitorForm.html", {"form":miForm})

def PlacaDeVideoForm(request):
    if request.method == "POST":
       miForm = placaDeVideoForm(request.POST)
       if miForm.is_valid():
           informacion = miForm.cleaned_data
           placas = placaDeVideo(marca = informacion['marca'], modelo = informacion['modelo'])
           placas.save()
           return render(request, "aplicacion/base.html")
    else:
       miForm = placaDeVideoForm()

    return render(request, "aplicacion/placaDeVideoForm.html", {"form":miForm})

def procesadorForm(request):
    if request.method == "POST":
        miForm = ProcesadorForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            procesadores = Procesador(marca = informacion['marca'], modelo = informacion['modelo'])
            procesadores.save()
            return render(request,"aplicacion/base.html")
    else:
        miForm = ProcesadorForm()
    
    return render(request, "aplicacion/procesadorForm.html", {"form":miForm})

def usuarioForm(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            usuarios = usuario(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion ['email'])
            usuarios.save()
            return render(request,"aplicacion/base.html")
    else:
        miForm = UsuarioForm()
    
    return render(request, "aplicacion/usuarioForm.html", {"form":miForm})


# BUSQUEDA DE MONITOR POR MARCA

def buscarmonitor(request):
    return render(request, "aplicacion/buscarmonitor.html")

def buscar2(request):
    if request.GET['marca']:
        marca = request.GET['marca']
        monitores = Monitor.objects.filter(marca_icontains=marca)
        return render(request, 
                      "aplicacion/resultadosMarca.html",
                      {"marca": marca, "monitores" : monitores})
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request,"aplicacion/base.html")

def procesador(request):
    return render(request,"aplicacion/procesador.html")

def placa_devideo(request):
    ctx = {"placadevideo": placaDeVideo.objects.all() }
    return render(request,"aplicacion/placadevideo.html", ctx)

def monitor(request):
    ctx = {"monitor": Monitor.objects.all() }
    return render(request,"aplicacion/monitor.html", ctx)

def usuario(request):
    return render(request,"aplicacion/usuario.html")
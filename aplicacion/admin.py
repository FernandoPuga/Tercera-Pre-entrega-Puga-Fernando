from django.contrib import admin
from .models import Procesador, placaDeVideo, Monitor, usuario

# Register your models here.

admin.site.register(Procesador)
admin.site.register(placaDeVideo)
admin.site.register(Monitor)
admin.site.register(usuario)

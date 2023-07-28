from django.db import models

# Create your models here.

class Procesador(models.Model):
     marca = models.CharField(max_length=50)
     modelo =  models.CharField(max_length=50)

     def __str__(self):
          return f"{self.marca}, {self.modelo}"


class placaDeVideo(models.Model):
     marca = models.CharField(max_length=50)
     modelo =  models.CharField(max_length=50)

     def __str__(self):
          return f"{self.marca}, {self.modelo}"

class Monitor(models.Model):
     marca = models.CharField(max_length=50)
     modelo = models.CharField(max_length=50)
     tamaño = models.IntegerField()

     def __str__(self):
          return f"{self.marca}, {self.modelo}, {self.tamaño}"

class usuario(models.Model):
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     email = models.EmailField()

     def __str__(self):
          return f"{self.nombre}, {self.apellido}, {self.email}"
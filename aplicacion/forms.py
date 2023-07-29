from django import forms

class MonitorForm(forms.Form):
    marca = forms.CharField(label = "Marca", max_length = 50, required = True)
    modelo = forms.CharField(label = "Modelo", max_length = 50, required = True)
    tamaño = forms.IntegerField(label = "Tamaño", required = True)

class placaDeVideoForm(forms.Form):
    marca = forms.CharField(label = "Marca", max_length = 50, required = True)
    modelo = forms.CharField(label = "Modelo", max_length = 50, required = True)
   
class ProcesadorForm(forms.Form):
    marca = forms.CharField(label = "Marca", max_length=50, required = True)
    modelo = forms.CharField(label = "Modelo",max_length=50, required=True)

class UsuarioForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length = 50, required = True)
    apellido = forms.CharField(label = "Apellido", max_length = 50, required = True)
    email = forms.EmailField(label = "Email", required = False)


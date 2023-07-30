# Tercera-Pre entrega- Python
#### Comisión: 43865
#### Alumno: Fernando Ariel Puga
## Nombre del Proyecto
Pagina de armado de PC

## Versión
1.0

## Descripción del Proyecto
Al ingreasar http://127.0.0.1:8000/aplicacion/ estaremos en el inicio de la pagina
Veremos 5 botonos (INICIO, MONITOR, PLACA DE VIDEO, PROCESADOR, USUARIO Y ADMINISTRADOR)
INICIO = volveremos a la pagina principal
MONITOR = Muestra los monitores que tenemos guardados
PLACA DE VIDEO = Muestra las placas que tenemos guardadas
PROCESADOR = Muestra los procesadores que tenemos guardados
USUARIO = Muestra los usuarios que tenemos guardados
ADMINISTRADOR = nos lleva al admin para poder realizar diferentes modificaciones.

Tambien podremos guardar nuestros diferentes componestes haciendo uso de Formularios que tenemos en form.py, especificacion de las urls para poder acceder a dichos formularios.
http://127.0.0.1:8000/aplicacion/monitor_form/
http://127.0.0.1:8000/aplicacion/placaDeVideo_form/
http://127.0.0.1:8000/aplicacion/procesador_form/
http://127.0.0.1:8000/aplicacion/usuario_form/

Por ultimo tenemos una busqueda con form, en este caso lo hice para mostrar los monitores que tengo guardados por marca
http://127.0.0.1:8000/aplicacion/buscar_monitor/

## Tecnología Utilizada

##### Front-End
- HTML 5
- CSS 3
##### Back-End
- Python 3.11.4
- Django 4.2.3

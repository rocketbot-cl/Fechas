



# Fechas
  
Módulo para manejar fechas  

*Read this in other languages: [English](Manual_Fechas.md), [Português](Manual_Fechas.pr.md), [Español](Manual_Fechas.es.md)*
  
![banner](imgs\Banner_fechas.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Formato Fechas
  
Cambia el formato a una fecha
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Fecha |Fecha a la cual se le cambiará el formato|19/10/2000|
|Resultado |Variable donde se almacenará el resultado|fecha|
|Formato de entrada|Formato que tiene la fecha ingresada|dd/mm/yyyy|
|Formato de salida |Formato que tendrá la fecha recibida|dd/mm/yyyy|
|Entrada personalizada |Si el formato de la fecha es diferente a las opciones anteriores, debe ingresarse en este campo.|%d/%m/%y|
|Salida personalizada |Si el formato de la fecha que se desea recibir es diferente a las opciones anteriores, debe ingresarse en este campo.|%d/%m/%y|

### Obtener dia de la semana
  
Obtiene el dia de la semana de la fecha ingresada. Por defecto 0 es lunes y 6 domingo.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Fecha |Campo para ingresar la fecha.|19/10/2000|
|Empezar día lunes del 1|Actívalo si deseas que el día lunes sea 1 en lugar de 0 como es por defecto.|False|
|Formato de entrada|Formato que tiene la fecha ingresada.|dd/mm/yyyy|
|Resultado |Variable donde se guardará el resultado.|fecha|

### Cálculo sobre fechas
  
Suma y resta valores en una fecha
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Fecha |Fecha que se utilizará en el cálculo|19/10/2000|
|Formato de entrada|Formato que tiene la fecha ingresada.|dd/mm/yyyy|
|Resultado |Variable donde se almacenará el resultado|fecha|
|Cantidad que será restada o sumada|Número que será restado o sumado de la fecha ingresada.|3|
|Tipo de fecha|Tipo de fecha que se desea restar o sumar|days|

### Obtener numero de la semana
  
Obtiene el numero de la semana.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Fecha |Fecha de la cual se desea obtener el numero de la semana|19/10/2000|
|Formato de entrada|Formato que tiene la fecha ingresada.|dd/mm/yyyy|
|Resultado |Variable donde se almacenará el resultado|fecha|

### Obtener numero de la semana del mes
  
Obtiene el numero de la semana del mes ingresado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Fecha |Fecha de la cual se desea obtener el numero de la semana|19/10/2000|
|Formato de entrada|Formato que tiene la fecha ingresada.|dd/mm/yyyy|
|Resultado |Variable donde se almacenará el resultado|fecha|

### Comparar Fechas
  
Comparar Fechas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Fecha 1 |Fecha 1 que se desea comparar|19/10/2000|
|Operación|Operación que se realizará entre las fechas ingresadas.|<|
|Fecha 2 |Fecha 2 que se desea comparar|19/10/2000|
|Resultado |Variable donde se almacenará el resultado|resultado|
|Formato de entrada|Formato que tiene la fecha ingresada|dd/mm/yyyy|
|Entrada personalizada |Completar en caso de que se desee utilizar otro formato de fecha.|%d/%m/%y|

### Días entre fechas
  
Este comando permite obtener la cantidad de días que hay entre dos fechas.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Fecha 1 |Fecha 1 que se desea comparar|30/10/2021|
|Fecha 2 |Fecha 2 que se desea comparar|10/10/2022|
|Formato de entrada|Formato que tiene la fecha ingresada|dd/mm/yyyy|
|Entrada personalizada |Completar en caso de que se desee utilizar otro formato de fecha.|%d/%m/%y|
|Resultado |Variable donde se almacenará el resultado|resultado|

### Obtener edad desde fecha de nacimiento
  
Obtiene la edad desde la fecha de nacimiento de una persona.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Fecha |Fecha de la cual se desea obtener la edad de la persona con el formato AAAA-MM-DD|AAAA-MM-DD|
|Resultado |Variable donde se almacenará el resultado|resultado|

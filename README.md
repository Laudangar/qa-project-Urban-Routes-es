# PROYECTO URBAN ROUTES 

Este proyecto contiene pruebas automatizadas para comprobar la funcionalidad de Urban Routes, que cubre el proceso de pedir un taxi. Con ello seleccionando la tarifa, llenado los datos requeridos para hacer el pedido, solicitando a su vez unas mantas y unos helados. Definiendo el paso a paso de este proseso.

REQUISITOS 

- Selenium
- Python
- pytest
- Servidor de Urban Routes

INSTALACIONES

1. Descarga de python
2. Descarga de Pytest desde PyCharm
3. Descarga de Git
4. Descarga de paquete selenium, desde el comando pip install
5. Descarga de paquete request, desde el comando pip install
5. Clonar el repositorio
6. Instalación de ChromeDriver

CONTENIDO 

El proyecto contine 6 carpetas, el las cuales se encuentra:
1. data.py: Dentro de este se almacena la información que se enviara en las solicitudes, así mismo las configuraciones para el proyecto en donde se almacenan la ruta al servidor.
2. main.py: Dentro de este se encuentra las pruebas para realizar el pedido del taxi.
3. Pages.py: Dentro de esta se encuentran los localizadores de las funciones relacionadas con las distintas páginas de tu aplicación
4. helpers.py: En esta se encuentra la funcionalidad retrieve_phone_code, el cual devuelve un número de confirmación de teléfono
5. README.md: El cual guarda la descripción del proyecto.
6. gitignore: En este se guardan archivos para que Git los descarte
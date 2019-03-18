# Demo: 
http://zrilae.pythonanywhere.com/


Saludos

Manual para probar este repositorio

Presets

- NOTA referente a la BD
      
      Esta aplicación cuenta con una tabla de registros precargada, en el directorio (//existe un script que puede ser modificado con la intención de optimizar la carga de archivos y generar nuevas coordenadas para posteriormente visualizarlas en el mapa. Dichos repositorios serán almacenados en un fichero de nombre app.db los cuales pueden ser visualizados con algun gestor de DB de sqlite3 p.e https://sqlitebrowser.org/. 
_____
![01](https://user-images.githubusercontent.com/19479856/54296526-bb2b1400-457a-11e9-8b80-a2cace21dc84.png)

_____
      
- Contar con alguna versión del lenguaje Python       
      https://www.python.org/downloads/

- Clonar el repositorio en el directorio destino

      git clone https://github.com/eberesquivel/flotilla.git
- Contar con pip actualizado

      pip install --upgrade pip
- Crear un entorno virtual de python con virtualenv
      
      pip install virtualenv : Comando para instalar librerías de virtualenv y crear dependencias
      virtualenv -p python3 env : Comando para crear entorno virtual en nuestro directorio y posteriormente descargar     dependencias requeridas para el funcionamiento de la app
      cd env
      source bin/activate: Este comando activará el entorno virtual de python
- Regresar al directorio raiz de la app
      
- Instalar las dependencias contenidas en el fichero requirements.txt
      
      pip install -r requirements.txt : Comando para instalar las dependecias del proyecto


- Nuestra aplicación está lista para iniciar
      
      python app.py :Este comando iniciará la aplicación en un servidor de prueba 
      
      127.0.0.1:5000:Dirección y puerto para acceder a la app
____

____

PANTALLAS GENERALES

Pantalla de inicio
![02](https://user-images.githubusercontent.com/19479856/54308219-1ec13b80-4593-11e9-8147-6306720ef417.png)

____
Pantalla de Busqueda

![03](https://user-images.githubusercontent.com/19479856/54308313-63e56d80-4593-11e9-9bc5-3ba80b62408a.png)

_____

Pantalla despliegue de Información
![04](https://user-images.githubusercontent.com/19479856/54308487-bb83d900-4593-11e9-8e44-9ed0534e15d6.png)

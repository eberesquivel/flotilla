Manual para probar este repositorio

Presets
- Contar con alguna versión del lenguaje Python 
      
      https://www.python.org/downloads/

- Clonar el repositorio en el directorio destino

      git clone https://github.com/eberesquivel/flotilla.git
- Contar con pip actualizado

      pip install --upgrade pip
- Crear un entorno virtual de python con virtualenv
      
      pip install virtualenv : Comando para instalar librerías de virtualenv y crear dependencias
      virtualenv env -p python3 : Comando para crear entorno virtual en nuestro directorio y posteriormente descargar     dependencias requeridas para el funcionamiento de la app
      cd env
      source bin/activate: Este comando activará el entorno virtual de python
- Regresar al directorio raiz de la app
      
- Instalar las dependencias contenidas en el fichero requirements.txt
      
      pip install -r requirements.txt : Comando para instalar las dependecias del proyecto


- Nuestra aplicación está lista para iniciar
      
      python app.py :Este comando iniciará la aplicación en un servidor de prueba 
      
      127.0.0.1:5000:Dirección y puerto para acceder a la app

# ApiRest D-BCH

This is an API Flask 

## Running Locally

Run the following commands to get started running this app locally:
```RUN: 
    . env/bin/activate
    flask run
```

Then visit `http://localhost:5000` to play with the app.

## Running Docker

```
    sudo docker container rm <container id>
    sudo docker build -t flaskapi:latest .
    sudo docker run --rm -it -v $(pwd)/api_flask:/api_flask -p 5000:8080 flaskapi
    sudo docker run --rm -it -v $(pwd)/api_flask:/api_flask -p 5000:5000 flaskapi sh
    sudo docker run --rm -it -v $(pwd)/api_flask:/api_flask -p 5000:5000 --network=host flaskapi
```
## Licensing

This example is open-sourced software licensed under the
[MIT license](https://opensource.org/licenses/MIT).

# Flask 2020
```
sudo easy_install pip

pip install virtualenv
virtualenv venv --python=python3.7
pip freeze
pip install -r requirements.txt
source venv/bin/activate

```
### HERE
```
verificar si el puerto 56733 esta en uso
sudo nc localhost 56733 < dev/null; echo $?
sudo bash start.sh
```
### Debugging en Flask
Debugging: es el proceso de identificar y corregir errores de programación.

Para activar el debug mode escribir lo siguiente en la consola:

```
export FLASK_DEBUG=1
echo $FLASK_DEBUG
````
### Request y Response
Logging: es una grabación secuencial en un archivo o en una base de datos de todos los eventos que afectan a un proceso particular.

Se utiliza en muchos casos distintos, para guardar información sobre la actividad de sistemas variados.

Tal vez su uso más inmediato a nuestras actividades como desarrolladores web sería el logging de accesos al servidor web, que analizado da información del tráfico de nuestro sitio. Cualquier servidor web dispone de logs con los accesos, pero además, suelen disponer de otros logs, por ejemplo, de errores.

Los sistemas operativos también suelen trabajar con logs, por ejemplo para guardar incidencias, errores, accesos de usuarios, etc.

A través de el logs se puede encontrar información para detectar posibles problemas en caso de que no funcione algún sistema como debiera o se haya producido una incidencia de seguridad.

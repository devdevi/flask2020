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
docker run --rm -it  -p 5000:80  --name=flask -v $PWD:/app flask sh
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

#!/bin/bash
app="flask"
docker build -t ${app} .
docker run --rm -it  -p 5000:80 \
 --name=${app} \
-v $PWD:/app ${app} sh

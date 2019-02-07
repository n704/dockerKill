#!/bin/bash

#entrypoint of the docker of the signal receive by docker will be redirected
# exec to change to load main program so that interrupt gets passed.
exec python ./app.py

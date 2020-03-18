# Kuting Game

this project shows how to deploy web app with Flask as backend on Heroku.

## Live demo
https://kt-game.herokuapp.com/

## QRCode library
Python:
1. OpenCV
2. pyzbar

Javascript:
1. JsQRScanner

## Reminder for deploying on Heroku when using pyzbar
1. run these cmd in terminal (install heroku CLI first):<br>
heroku buildpacks:add --index 1 heroku-community/apt --app kt-game
heroku create --buildpack https://github.com/generalui/heroku-buildpack-zbar.git


2. create "Aptfile" on the same folder of app.py. And put the content inside this file<br>
libzbar0
libzbar-dev

3. duplicate pyzbar package into the same folder of app.py.<br>

4. replace "find_library" to hard code path<br>
path = find_library('zbar') ---> path = '/app/.apt/usr/lib/x86_64-linux-gnu/libzbar.so'


## Third-party library
JsQRScanner (https://github.com/jbialobr/JsQRScanner)

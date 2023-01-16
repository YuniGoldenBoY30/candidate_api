#!/bin/sh
@echo off
echo Creando migraciones...
echo.
python manage.py makemigrations
echo.
echo Creando modelo de datos ...
echo.
python manage.py migrate
echo.
echo Cargando datos iniciales ...
echo.
python manage.py loaddata initial_data.json

echo.
echo Carga inicial concluida satisfactoriamente ...


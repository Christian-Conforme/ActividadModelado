@echo off

rem Detener la aplicación si está en ejecución
tasklist /FI "WINDOWTITLE eq Python"* | findstr /I "python.exe"
if %ERRORLEVEL% == 0 (
    echo Deteniendo la aplicación...
    taskkill /F /IM python.exe
)

rem Iniciar la aplicación
echo Iniciando la aplicación...
start /B python app.py

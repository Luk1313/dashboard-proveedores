@echo off
cd /d "%~dp0"
echo === Activando entorno virtual ===
if not exist .venv (
    echo No existe entorno. Creando con Python 3.11...
    py -3.11 -m venv .venv
)
call .venv\Scripts\activate.bat
echo === Instalando dependencias ===
pip install -r requirements.txt
echo === Ejecutando el dashboard ===
python main.py
pause

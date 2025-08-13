@echo off
setlocal
echo === GenericDiscordRPC - Instalador (Windows) ===
python --version || (echo Python no esta en PATH & pause & exit /b 1)

REM (Opcional) crear venv
REM python -m venv .venv
REM call .venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Listo. Ejecuta:  python src\main.py
pause

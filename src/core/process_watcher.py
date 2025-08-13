"""
process_watcher.py
Vigila si un proceso con un nombre exacto está ejecutándose.
- Usa psutil para iterar procesos en el sistema.
- Ajusta PROCESS_NAME para tu programa objetivo.
"""

import psutil

# Cambia este valor por el nombre del proceso que quieras vigilar.
# En Windows suele ser algo como "notepad.exe" o "Ssms.exe".
# En Mac/Linux, el binario sin extensión, por ejemplo "Code" o "postgres".
PROCESS_NAME = "notepad.exe"

def is_process_running() -> bool:
    """Devuelve True si el proceso con nombre exacto está activo."""
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info.get('name') == PROCESS_NAME:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

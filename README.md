# GenericDiscordRPC
---

Proyecto genérico para conectar **cualquier programa** a **Discord Rich Presence** usando Python y `pypresence`.  
Arquitectura sencilla en capas para que puedas extenderlo rápido.
---

## Autor

    ElPsyCongroo 

---

## Estructura

```
GenericDiscordRPC/
├── README.md
├── requirements.txt
├── install_windows.bat
├── install_unix.sh
└── src/
    ├── __init__.py
    ├── main.py
    ├── core/
    │   ├── __init__.py
    │   ├── process_watcher.py
    │   ├── discord_rpc.py
    │   └── notifier.py
    └── utils/
        ├── __init__.py
        └── logger.py
```

### Qué hace cada archivo

- `src/main.py`: Punto de entrada. Coordina watcher + RPC + notificaciones.
- `src/core/process_watcher.py`: Detecta si *tu* proceso está corriendo.
- `src/core/discord_rpc.py`: Conecta, actualiza y limpia Discord RPC.
- `src/core/notifier.py`: Notificaciones nativas (Windows/Mac/Linux).
- `src/utils/logger.py`: Logging a consola y archivo.

---

## Requisitos

- Python 3.8+
- Tener abierto **Discord Desktop** (no web)
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

### Paquetes
- `pypresence` (Rich Presence)
- `psutil` (detección de procesos)

---

## Instalación rápida

### Windows
Haz doble clic en `install_windows.bat`

### Mac / Linux
```bash
chmod +x install_unix.sh
./install_unix.sh
```

---

## Uso

1) Edita el nombre del proceso a vigilar en `src/core/process_watcher.py`:
```python
PROCESS_NAME = "notepad.exe"  # <- cámbialo por tu app
```

2) Edita tu **Discord Application ID** en `src/main.py`:
```python
CLIENT_ID = "TU_APPLICATION_ID"
```

3) Ejecuta:
```bash
python src/main.py
```

Cuando el proceso esté activo, verás tu Rich Presence en Discord.  
Cuando se cierre, se limpia automáticamente.

---

## Personalización rápida

- Cambia los textos e imágenes del RPC en `src/core/discord_rpc.py` → `update_rpc`.
- Para imágenes personalizadas, súbelas en el **Discord Developer Portal** de tu app y usa sus *keys* en `large_image` / `small_image`.

---

## Solución de problemas

- **No aparece el estado en Discord**: Asegúrate de tener la app de **Discord Desktop** abierta.
- **Pylance marca imports en VS Code web**: es normal si no hay entorno local. En tu máquina, instala dependencias y todo se resuelve.
- **Notificaciones en Linux**: necesitas `notify-send` (paquete `libnotify-bin` en Debian/Ubuntu).

---

## Licencia

MIT License © 2025 ElPsyCongroo

---

### ¡Gracias por usar Generic Discord RPC!

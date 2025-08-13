"""
discord_rpc.py
Conecta y actualiza Discord Rich Presence.
- Requiere tener Discord Desktop abierto.
- Usa pypresence.Presence para la conexión RPC.
"""

from pypresence import Presence, DiscordNotFound, InvalidPipe
import time
import utils.logger as logger

def connect_rpc(client_id: str):
    """Intenta conectar al pipe de Discord y devolver el objeto Presence."""
    try:
        rpc = Presence(client_id)
        rpc.connect()
        return rpc
    except DiscordNotFound:
        logger.log("Discord Desktop no encontrado. Abre la app de Discord.")
        return None
    except InvalidPipe:
        logger.log("InvalidPipe al conectar RPC. Reintentará cuando el proceso siga activo.")
        return None
    except Exception as e:
        logger.log(f"Error conectando RPC: {type(e).__name__} - {e}")
        return None

def update_rpc(rpc):
    """
    Actualiza el Rich Presence.
    Personaliza los textos e imágenes según tu app de Discord.
    - 'large_image': debe existir en tu app (Assets > Rich Presence > Art Assets)
    """
    if not rpc:
        return
    try:
        rpc.update(
            details="Ejecutando programa genérico",
            state="Estado: activo",
            large_image="default_image",  # <- cambia por el key de tu imagen
            start=int(time.time())
        )
    except Exception as e:
        logger.log(f"Error actualizando RPC: {type(e).__name__} - {e}")

def disconnect_rpc(rpc):
    """Limpia y cierra la conexión RPC si existe."""
    try:
        if rpc:
            try:
                rpc.clear()
            except Exception:
                pass
            try:
                rpc.close()
            except Exception:
                pass
    except Exception:
        pass

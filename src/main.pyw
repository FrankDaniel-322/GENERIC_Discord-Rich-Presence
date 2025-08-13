"""
main.py
Punto de entrada del proyecto GenericDiscordRPC.
- Vigila un proceso (core/process_watcher.py)
- Conecta/actualiza Discord Rich Presence (core/discord_rpc.py)
- Muestra notificaciones nativas (core/notifier.py)
"""

from core import process_watcher, discord_rpc, notifier
from utils import logger
import time

# TODO: Cambia esto por el Application ID de TU app de Discord.
CLIENT_ID = "1404602960700379267"

CHECK_INTERVAL = 2  # segundos entre comprobaciones

def main():
    logger.log("Iniciando Generic Discord RPC.")
    notifier.notify("Generic Discord RPC", "Vigilante iniciado.")
    rpc = None
    presence_active = False

    try:
        while True:
            running = process_watcher.is_process_running()
            if running and not presence_active:
                logger.log("Proceso detectado -> conectando Discord RPC...")
                rpc = discord_rpc.connect_rpc(CLIENT_ID)
                if rpc:
                    discord_rpc.update_rpc(rpc)
                    presence_active = True
                    logger.log("Discord RPC conectado y actualizado.")
                    notifier.notify("Generic Discord RPC", "Proceso activo y conectado a Discord.")
            elif not running and presence_active:
                logger.log("Proceso detenido -> limpiando Discord RPC...")
                discord_rpc.disconnect_rpc(rpc)
                rpc = None
                presence_active = False
                notifier.notify("Generic Discord RPC", "Proceso cerrado, presencia limpiada.")

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        logger.log("Interrupción por teclado. Saliendo...")
    finally:
        discord_rpc.disconnect_rpc(rpc)
        logger.log("Servicio terminado.")

if __name__ == "__main__":
    main()

"""
logger.py
Registra mensajes con timestamp en consola y en archivo local.
"""

from datetime import datetime
from typing import Any

LOG_PATH = "generic_discord_rpc.log"

def log(msg: Any) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

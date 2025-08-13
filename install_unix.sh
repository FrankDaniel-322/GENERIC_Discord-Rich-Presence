#!/usr/bin/env bash
set -euo pipefail
echo "=== GenericDiscordRPC - Instalador (Unix) ==="
python3 --version || { echo "Python3 no esta en PATH"; exit 1; }

# (Opcional) crear venv
# python3 -m venv .venv
# source .venv/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo
echo "Listo. Ejecuta:  python3 src/main.py"

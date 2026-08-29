#!/bin/bash
set -e
sudo apt update
sudo apt install -y python3-venv
VENV_DIR="$HOME/.wsl_venv"
python3 -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install --upgrade pip setuptools wheel
"$VENV_DIR/bin/pip" install torch torchvision --index-url https://download.pytorch.org/whl/cpu
"$VENV_DIR/bin/python" - <<'PY'
import torch, torchvision
print('torch', torch.__version__)
print('torchvision', torchvision.__version__)
PY

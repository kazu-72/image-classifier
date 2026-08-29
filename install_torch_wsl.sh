#!/bin/bash
set -e
sudo apt update
sudo apt install -y python3-venv
python3 -m venv /mnt/c/Users/hp/Downloads/data/.wsl_venv
/mnt/c/Users/hp/Downloads/data/.wsl_venv/bin/python -m pip install --upgrade pip setuptools wheel
/mnt/c/Users/hp/Downloads/data/.wsl_venv/bin/pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
/mnt/c/Users/hp/Downloads/data/.wsl_venv/bin/python - <<'PY'
import torch, torchvision
print('torch', torch.__version__)
print('torchvision', torchvision.__version__)
PY

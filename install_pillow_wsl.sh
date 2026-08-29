#!/bin/bash
set -e
if python3 -m pip --version >/dev/null 2>&1; then
  echo "pip present"
else
  sudo apt update
  sudo apt install -y python3-pip
fi
python3 -m pip install --user --upgrade pillow
python3 -c 'from PIL import Image; print("Pillow", Image.__version__)'

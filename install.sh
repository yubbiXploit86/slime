#!/bin/bash
set -e
python3 -m venv slime-env
source slime-env/bin/activate
pip install -r requirements.txt
chmod +x slime.py
sudo ln -sf $(pwd)/slime.py /usr/bin/slime
cp banner.txt ~/.slime_banner
echo "[+] SLIME ready. Run: slime <url>"

# SLIME Security Inspector

Audit‑grade **defensive web security engine** for authorized testing.
Built for **accuracy, stability, and low false‑positives**.

## Highlights
- Context‑aware detection (XSS/SQLi)
- Differential analysis (baseline vs injected)
- Evidence‑weighted risk scoring
- Clean, aesthetic CLI output

## Features
- Deep parameter discovery (URL + GET forms)
- XSS reflected detection (HTML/ATTR/JS)
- SQL injection indication (error‑based + behavioral)
- Cookie security analysis
- Security headers & TLS posture
- Risk levels: LOW / MEDIUM / HIGH / CRITICAL

## NOTE !! FOR LINUX ONLY ‼️‼️
## Install
```bash
git clone https://github.com/yubbiXploit86/slime.git
cd slime
chmod +x install.sh
./install.sh


Usage : slime https://example.com/page.php?id=1

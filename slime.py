#!/usr/bin/env python3
# SLIME – Defensive Web Security Inspector (Authorized Use Only)

import os, sys, requests
from termcolor import colored
from engine.discovery import discover_params
from engine.xss import detect_xss
from engine.sqli import detect_sqli
from engine.cookies import analyze_cookies
from engine.headers import analyze_headers
from engine.risk import risk_label

TIMEOUT=10
BANNER=os.path.expanduser("~/.slime_banner")

def c(t,col): return colored(t,col)
def log(tag,msg,col): print(c(f"[{tag}] ",col)+msg)

def banner():
    try: print(c(open(BANNER).read(),"cyan"))
    except: print(c("SLIME SECURITY INSPECTOR\n","cyan"))

def fetch(url, params=None):
    if params: return requests.get(url, params=params, timeout=TIMEOUT, allow_redirects=True)
    return requests.get(url, timeout=TIMEOUT, allow_redirects=True)

def main():
    banner()
    if len(sys.argv)<2:
        log("ERR","Gunakan: slime <url>","red"); sys.exit(1)
    url=sys.argv[1]
    log("INFO",f"Target: {url}","blue")

    r=fetch(url)
    params=discover_params(url, r.text)
    if params: log("INFO","Parameter: "+", ".join(params),"blue")
    else: log("OK","Tidak ada parameter","green")

    risk=0

    xss=detect_xss(fetch, url, params)
    for f in xss:
        log("VULN",f"XSS Reflected [{'/'.join(f['contexts'])}] pada '{f['param']}' | conf {f['confidence']}","red")
        risk+=3

    sqli=detect_sqli(fetch, url, params)
    for f in sqli:
        log("VULN",f"SQLi indikatif pada '{f['param']}' | conf {f['confidence']}","red")
        risk+=4

    for w in analyze_cookies(r.cookies):
        log("WARN",f"Cookie {w['name']} → {', '.join(w['issues'])}","yellow"); risk+=1

    miss=analyze_headers(r.headers)
    if miss:
        log("WARN","Header hilang: "+", ".join(miss),"yellow"); risk+=1

    label,col=risk_label(risk)
    print(); log("RISK",label,col)
    log("INFO","Audit selesai (defensive, non‑destruktif)","blue")

if __name__=="__main__":
    main()

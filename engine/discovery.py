from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

def discover_params(url, html):
    params=set(parse_qs(urlparse(url).query).keys())
    soup=BeautifulSoup(html,"html.parser")
    for f in soup.find_all("form"):
        if f.get("method","").lower()=="get":
            for i in f.find_all("input"):
                if i.get("name"): params.add(i["name"])
    return sorted(p for p in params if p)

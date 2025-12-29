import re
SQL_ERR=re.compile(r"(sql syntax|mysql|postgresql|sqlite|ora-|mssql)",re.I)

def detect_sqli(fetch, url, params):
    base=url.split("?")[0]
    out=[]
    for p in params:
        r0=fetch(base,{p:"1"})
        r1=fetch(base,{p:"'"})
        err=bool(SQL_ERR.search(r1.text))
        beh=abs(len(r0.text)-len(r1.text))>200 or r1.status_code!=r0.status_code
        if err or beh:
            out.append({"param":p,"confidence":0.9 if err and beh else 0.72})
    return out

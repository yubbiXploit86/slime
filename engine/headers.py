REQ=["Content-Security-Policy","X-Frame-Options",
     "X-Content-Type-Options","Strict-Transport-Security","Referrer-Policy"]
def analyze_headers(h): return [x for x in REQ if x not in h]

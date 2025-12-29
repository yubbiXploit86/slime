def analyze_cookies(cookies):
    issues=[]
    for c in cookies:
        f=[]
        if not c.secure: f.append("Secure missing")
        if not c.has_nonstandard_attr("HttpOnly"): f.append("HttpOnly missing")
        if not c.has_nonstandard_attr("SameSite"): f.append("SameSite missing")
        if f: issues.append({"name":c.name,"issues":f})
    return issues

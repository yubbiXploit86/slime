def detect_xss(fetch, url, params):
    base=url.split("?")[0]
    markers=["slx","slx_attr","slx_js"]
    out=[]
    for p in params:
        ctx=set()
        for m in markers:
            payload=f"<{m}>"
            r=fetch(base,{p:payload})
            if payload in r.text:
                c="HTML"
                if f'="{payload}"' in r.text: c="ATTR"
                if f"'{payload}'" in r.text: c="JS"
                ctx.add(c)
        if ctx:
            out.append({"param":p,"contexts":list(ctx),
                        "confidence":0.9 if len(ctx)>1 else 0.78})
    return out

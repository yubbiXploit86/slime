def risk_label(score):
    if score>=9: return ("CRITICAL","red")
    if score>=6: return ("HIGH","red")
    if score>=3: return ("MEDIUM","yellow")
    return ("LOW","green")

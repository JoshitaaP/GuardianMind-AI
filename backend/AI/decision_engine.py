def decide(result):
    risk=result["risk"]
    if risk>=90:
        result["action"]="block"
    elif risk>=60:
        result["action"]="warn"
    else:
        result["action"]="allow"
    return result
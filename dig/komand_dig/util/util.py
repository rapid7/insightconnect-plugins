def safe_parse(re):
    re = re.group(1) if re else "NO MATCHES FOUND"
    return re

def not_empty(re):
    return False if re == "NO MATCHES FOUND" else True

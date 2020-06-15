import re

def determine_address_type(address: str) -> str:
    # ':' is not allowed in domain name or IPv4 IP Address (only allowed in IPv6)
    if re.search(':', address):
        return "ipv6"
    if re.search('[a-zA-Z]', address):
        return "fqdn"
    if re.search('/', address):
        return "cidr"
    return "ipv4"
from ipaddress import ip_address
import re

MAC_ADDRESS = "Mac Address"
IP_ADDRESS = "IP Address"
HOSTNAME = "Host Name"
DEVICE_ID = "Device ID"

def get_agent_type(search_string):
    try:
        search_string = ip_address(search_string)
        return IP_ADDRESS
    except Exception:
        pass

    mac_address_regex = re.compile("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")
    if mac_address_regex.match(search_string):
        return MAC_ADDRESS

    try:
        int(search_string)
        return DEVICE_ID
    except Exception:
        pass

    return HOSTNAME

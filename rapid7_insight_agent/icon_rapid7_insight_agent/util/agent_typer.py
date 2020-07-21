from ipaddress import ip_address
import re

MAC_ADDRESS = "Mac Address"
IP_ADDRESS = "IP Address"
HOSTNAME = "Host Name"
# DEVICE_ID = "Device ID" # Device ID is a 32 len hex string. It's unlikely but possible that matches a hostname.

def get_agent_type(search_string):
    try:
        search_string = ip_address(search_string)
        return IP_ADDRESS
    except Exception:
        pass # Not an IP

    mac_regex = "^(((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2})$|^(((\d|([a-f]|[A-F])){2}-){5}(\d|([a-f]|[A-F])){2})$|^$"
    mac_reg = re.compile(mac_regex)
    if mac_reg.match(search_string):
        return MAC_ADDRESS

    return HOSTNAME

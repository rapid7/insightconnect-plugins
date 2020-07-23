from ipaddress import ip_address
import re

MAC_ADDRESS = "Mac Address"
IP_ADDRESS = "IP Address"
HOSTNAME = "Host Name"
# DEVICE_ID = "Device ID" # Device ID is a 32 len hex string. It's unlikely but possible that matches a hostname.
REGEX_STRING = "^(?:[0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2})$"
MAC_REGEX = re.compile(REGEX_STRING)

def get_agent_type(search_string):
    try:
        search_string = ip_address(search_string)
        return IP_ADDRESS
    except ValueError:
        pass # Not an IP

    if MAC_REGEX.match(search_string):
        return MAC_ADDRESS

    return HOSTNAME

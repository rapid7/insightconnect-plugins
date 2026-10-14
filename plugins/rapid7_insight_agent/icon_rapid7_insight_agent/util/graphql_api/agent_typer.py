from ipaddress import ip_address
import re

MAC_ADDRESS = "Mac Address"
IP_ADDRESS = "IP Address"
HOSTNAME = "Host Name"
# DEVICE_ID = "Device ID" # Device ID is a 32 len hex string. It's unlikely but possible that matches a hostname.
REGEX_STRING = (
    "^(?:[0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2})$"
)
MAC_REGEX = re.compile(REGEX_STRING)
AGENT_ID_REGEX = re.compile("^[0-9a-fA-F]{32}$")


def looks_like_agent_id(search_string: str) -> bool:
    """
    Check whether the string has the shape of an agent ID (32 hex characters, dashes ignored)

    :param search_string: string
    :return: bool
    """
    return bool(AGENT_ID_REGEX.match(search_string.replace("-", "")))


def get_agent_type(search_string: str) -> str:
    """
    Get the type of agent from the agent string

    :param search_string: string
    :return: string
    """
    try:
        search_string = ip_address(search_string)
        return IP_ADDRESS
    except ValueError:
        pass  # Not an IP

    if MAC_REGEX.match(search_string):
        return MAC_ADDRESS

    return HOSTNAME

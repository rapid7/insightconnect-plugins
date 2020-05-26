from enum import Enum
import ipaddress


class DetailsLevel(Enum):
    uid = "uid"
    standard = "standard"
    full = "full"


def check_if_ip_in_whitelist(ip_address: str, whitelist: [str]) -> bool:
    """
    Check if an IP address is in a whitelist
    :param ip_address: IP address to check for
    :param whitelist: List of IP addresses/CIDR IP addresses to check against
    :return: True if the IP address is found
    """

    # First pass check to see if it's in the raw list
    if ip_address in whitelist:
        return True

    # IP address not present, so now iterate through subnets
    ip_obj = ipaddress.ip_address(ip_address)

    networks = {ipaddress.ip_network(item) for item in whitelist if "/" in item}

    for network in networks:
        if ip_obj in network:
            return True

    return False

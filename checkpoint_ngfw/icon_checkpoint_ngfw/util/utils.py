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

    for item in whitelist:
        if "/" in item:
            # handle CIDR
        elif ipaddress.
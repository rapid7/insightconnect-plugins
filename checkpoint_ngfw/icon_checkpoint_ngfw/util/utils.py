from enum import Enum
import ipaddress


class PublishException(Exception):

    def __init__(self, code: str, message: str, errors: [dict]):
        super().__init__()

        self.code = code
        self.message = message
        self.errors = errors

    @classmethod
    def from_json_response(cls, json_: dict):
        return cls(
            code=json_.get("code", ""),
            message=json_.get("message", ""),
            errors=json_.get("errors")
        )

    def get_errors(self) -> [str]:
        return {e.get("message") for e in self.errors if e.get("message") is not None}


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

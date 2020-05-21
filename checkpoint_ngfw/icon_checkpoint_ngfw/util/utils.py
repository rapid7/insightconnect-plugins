from enum import Enum
import re
from ipaddress import ip_address, ip_network


class DetailsLevel(Enum):
    uid = "uid"
    standard = "standard"
    full = "full"


class AddressType(Enum):
    fqdn = "fqdn"
    cidr = "cidr"
    ip = "ip"
    unknown = "unknown"


class IPAddressCheck:

    @staticmethod
    def determine_address_type(address: str) -> AddressType:
        """
        Check a user-input address and determine if it is a FQDN, IP address, or CIDR IP address
        :param address:
        :return:
        """
        if re.search('[a-zA-Z]', address):
            return AddressType.fqdn
        if re.search('/', address):
            return AddressType.cidr
        try:
            if ip_address(address=address):
                return AddressType.ip
        except ValueError:
            pass

        return AddressType.unknown  # This could be wildcard, in which case we can't handle it elegantly

    @staticmethod
    def check_ip_in_range(ip: str, cidr: str) -> bool:
        ip = ip_address(ip)
        net = ip_network(cidr, False)
        return ip in net

    @staticmethod
    def check_address_against_object(address_object, address_to_check):
        address_type = self.determine_address_type(address_to_check)
        object_type = self.determine_address_type(address_object)

        if object_type == "fqdn" or object_type == "ip_address":
            return address_object == address_to_check

        if object_type == "ip_range":
            if address_type == "ip_address":
                return self.check_ip_in_range(address_to_check, address_object)

        return False
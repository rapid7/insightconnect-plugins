import re
from ipaddress import ip_address, ip_network


class IpCheck:
    def determine_address_type(self, address) -> str:
        try:
            if ip_address(address):
                return "ip_address"
        except ValueError:
            pass
        if re.search("[a-zA-Z]", address):
            return "fqdn"
        if re.search("/", address):
            return "ip_range"

        return "unknown"  # This could be wildcard, in which case we can't handle it elegantly

    def check_ip_in_range(self, ip: str, cidr: str) -> bool:
        ip = ip_address(ip)
        net = ip_network(cidr, False)
        return ip in net

    def check_address_against_object(self, address_object, address_to_check):
        address_type = self.determine_address_type(address_to_check)
        object_type = self.determine_address_type(address_object)

        if object_type in ("fqdn", "ip_address"):
            return address_object == address_to_check

        if object_type == "ip_range":
            if address_type == "ip_address":
                return self.check_ip_in_range(address_to_check, address_object)

        return False

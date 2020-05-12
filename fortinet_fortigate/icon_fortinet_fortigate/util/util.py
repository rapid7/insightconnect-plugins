import re
from ipaddress import ip_network, ip_address


class Helpers(object):

    def __init__(self, logger):
        """
        Creates a new instance of Helpers
        :param logger: Logger object available to Komand actions/triggers, usually self.logger
        :return: Helpers object
        """
        self.logger = logger

    @staticmethod
    def determine_address_type(address):
        if re.search('[a-zA-Z]', address):
            return "fqdn"
        return "ipmask"

    def match_whitelist(self, address: str, whitelist: list) -> bool:
        """
        Checks to see if the address is in the white list
        :param address: An IP mask or a FQDN
        :param whitelist: A list of IP masks and FQDN's to check against
        :return: If the address was in the whitelist
        """
        object_type = self.determine_address_type(address)
        if object_type == "fqdn":
            if address in whitelist:
                self.logger.info(f" Whitelist matched\n{address} was found in whitelist")
                return True
            else:
                return False

        # if 1.1.1.1/32 - remove /32
        trimmed_address = re.sub(r"/32$", "", address)

        # if contains / we compare explicit matches, but not subnets in subnets
        if '/' in trimmed_address:
            return address in whitelist

        # IP is in CIDR - Give the user a log message
        for item in whitelist:
            type_ = self.determine_address_type(item)
            if type_ == "ipmask":
                net = ip_network(item,
                                 False)  # False means ignore the masked bits, otherwise they need to be 0
                ip = ip_address(trimmed_address)
                if ip in net:
                    self.logger.info(f" Whitelist matched\nIP {address} was found in {item}")
                    return True

        return False

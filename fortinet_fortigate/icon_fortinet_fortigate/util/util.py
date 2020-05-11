import re
from ipaddress import ip_network, ip_address


class Whitelist(object):

    def __init__(self, logger):
        """
        Creates a new instance of ResourceHelper
        :param logger: Logger object available to Komand actions/triggers, usually self.logger
        :return: Whitelist object
        """
        self.logger = logger

    @staticmethod
    def determine_address_type(address):
        if re.search('[a-zA-Z]', address):
            return "fqdn"
        if re.search('/', address):
            return "ip-netmask"
        return "ip-netmask"

    def match_whitelist(self, address: str, whitelist: list, object_type: str) -> bool:
        """
        Checks to see if the address is in the white list
        :param address:
        :param whitelist:
        :param object_type:
        :return:
        """
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
            if type_ == "ip-netmask":
                net = ip_network(item,
                                 False)  # False means ignore the masked bits, otherwise they need to be 0
                ip = ip_address(trimmed_address)
                if ip in net:
                    self.logger.info(f" Whitelist matched\nIP {address} was found in {item}")
                    return True

        return False

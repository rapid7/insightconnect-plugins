from ipwhois import IPWhois
from logging import Logger


class IPWhoisLookup:
    def __init__(self, logger: Logger):
        self._logger = logger

    def perform_lookup_rdap(self, ip_address: str) -> dict:
        try:
            return IPWhois(ip_address).lookup_rdap(depth=1)
        except:
            self._logger.warning("Couldn't find info about ASN for given IP. ASN result is empty.\n")
            return {}

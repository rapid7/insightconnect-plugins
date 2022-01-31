import re
from ipaddress import ip_network, ip_address, IPv4Network
from insightconnect_plugin_runtime.exceptions import PluginException
import validators
import urllib.parse


class Helpers(object):

    # status codes constant. Used to id all non 2XX return codes and there causes and assistance
    _STATUS_CODES = {
        400: {
            "cause": "Bad Request: Request cannot be processed by the API.",
            "assistance": "Contact support for assistance.",
        },
        401: {
            "cause": "Not Authorized: Request without successful login session.",
            "assistance": "Ensure that the API key is correct,"
            " and that the IP address of the orchestrator has been added to the trusted hosts list",
        },
        403: {
            "cause": "Forbidden: Request is missing CSRF token or administrator is missing access profile permissions.",
            "assistance": "Ensure that the account being used has permission to preform this action.",
        },
        404: {
            "cause": "Resource Not Found: Unable to find the specified resource.",
            "assistance": "Data was requested but not found. Check that inputs are correct.",
        },
        405: {
            "cause": "Method Not Allowed: Specified HTTP method is not allowed for this resource.",
            "assistance": "Contact support for assistance.",
        },
        413: {
            "cause": "Request Entity Too Large: Request cannot be processed due to large entity.",
            "assistance": "Contact support for assistance.",
        },
        424: {
            "cause": "Failed Dependency: Fail dependency can be duplicate resource, missing required parameter,"
            " missing required attribute, invalid attribute value.",
            "assistance": "This error is caused because a required condition was not met."
            " Common caused are: trying to add a object that already exists,"
            " or trying to delete an object that is currently in use.",
        },
        429: {
            "cause": "Access temporarily blocked: Maximum failed authentications reached."
            " The offended source is temporarily blocked for certain amount of time.",
            "assistance": "Wait out the access timeout.",
        },
        500: {
            "cause": "Internal Server Error: Internal error when processing the request.",
            "assistance": "Something went wrong and the API did not provide a reason. This can happen when an object "
            "you're trying to create already exists or when an object you're trying to remove doesn't exist. If the "
            "issue persists contact support for additional assistance.",
        },
    }

    def __init__(self, logger):
        """
        Creates a new instance of Helpers
        :param logger: Logger object available to Komand actions/triggers, usually self.logger
        :return: Helpers object
        """
        self.logger = logger

    def http_errors(self, response: dict, status_code: int) -> None:
        """
        Will look for and handle non 2XX status codes
        :param response: The JSON response from the API call
        :param status_code: The API calls status code
        """
        if status_code in self._STATUS_CODES:
            raise PluginException(
                cause=self._STATUS_CODES[status_code]["cause"],
                assistance=self._STATUS_CODES[status_code]["assistance"],
                data=response,
            )
        if status_code not in range(200, 299):
            raise PluginException(
                cause="An undocumented response code was returned.",
                assistance="Contact support for assistance",
                data=response,
            )

    @staticmethod
    def determine_address_type(address: str) -> str:
        if validators.domain(address):
            return "fqdn"
        if validators.ipv4(address) or validators.ipv4_cidr(address):
            return "ipmask"
        if validators.ipv6(address) or validators.ipv6_cidr(address):
            return "ipprefix"
        else:
            raise PluginException(
                cause=f"The type could not be determined for the given address: {address}.",
                assistance="Please check that provided address is correct and try again.",
            )

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
                self.logger.info(f"Whitelist matched. The domain {address} was found on the whitelist.")
                return True
            else:
                return False

        if object_type == "ipmask":
            # if 1.1.1.1/32 - remove /32
            trimmed_address = re.sub(r"/32$", "", address)
        else:
            trimmed_address = re.sub(r"/128$", "", address)

        # if contains / we compare explicit matches, but not subnets in subnets
        if "/" in trimmed_address:
            return address in whitelist

        # IP is in CIDR - Give the user a log message
        for item in whitelist:
            type_ = self.determine_address_type(item)
            if type_ == object_type:
                net = ip_network(item, False)  # False means ignore the masked bits, otherwise they need to be 0
                ip = ip_address(trimmed_address)
                if ip in net:
                    self.logger.info(f"Whitelist matched.\nThe IP address {address} was found on the whitelist.")
                    return True

        return False

    @staticmethod
    def ipmask_converter(host: str) -> str:
        """Converts a IP or netmask into a CIDR"""
        try:
            host = ip_network(host)
        except ValueError:
            host = host.replace(" ", "/")
            host = ip_network(host)
        return str(host)

    @staticmethod
    def netmask_converter(host: str) -> str:
        """Converts a CIDR or IP to a netmask"""
        host = IPv4Network(host).with_netmask
        host = str(host)
        host = host.replace("/", " ")
        return host

    @staticmethod
    def url_encode(string: str) -> str:
        return urllib.parse.quote(string, safe="")

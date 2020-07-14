import re
from ipaddress import ip_network, ip_address, IPv4Network
from komand.exceptions import PluginException


class Helpers(object):

    # status codes constant. Used to id all non 2XX return codes and there causes and assistance
    _STATUS_CODES = {
        400: {"cause": "Bad Request: Request cannot be processed by the API.",
              "assistance": "Contact support for assistance."},
        401: {"cause": "Not Authorized: Request without successful login session.",
              "assistance": "Ensure that the API key is correct,"
                            " and that the IP address of the orchestrator has been added to the trusted hosts list"},
        403: {"cause": "Forbidden: Request is missing CSRF token or administrator is missing access profile permissions.",
              "assistance": "Ensure that the account being used has permission to preform this action."},
        404: {"cause": "Resource Not Found: Unable to find the specified resource.",
              "assistance": "Data was requested but not found. Check that inputs are correct."},
        405: {"cause": "Method Not Allowed: Specified HTTP method is not allowed for this resource.",
              "assistance": "Contact support for assistance."},
        413: {"cause": "Request Entity Too Large: Request cannot be processed due to large entity.",
              "assistance": "Contact support for assistance."},
        424: {"cause": "Failed Dependency: Fail dependency can be duplicate resource, missing required parameter,"
                       " missing required attribute, invalid attribute value.",
              "assistance": "This error is caused because a required condition was not met."
                            " Common caused are: trying to add a object that already exists,"
                            " or trying to delete an object that is currently in use."},
        429: {"cause": "Access temporarily blocked: Maximum failed authentications reached."
                       " The offended source is temporarily blocked for certain amount of time.",
              "assistance": "Wait out the access timeout."},
        500: {"cause": "Internal Server Error: Internal error when processing the request.",
              "assistance": "Something went wrong and the API did not provide a reason."
                            "This can happen when an object you're trying to create already exists or when an object you're trying to remove doesn't exist."
                            "If the issue persists contact support for additional assistance."}
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
            raise PluginException(cause=self._STATUS_CODES[status_code]["cause"],
                                  assistance=self._STATUS_CODES[status_code]["assistance"],
                                  data=f"Raw response data: {response}")
        if status_code not in range(200, 299):
            raise PluginException(cause="An undocumented response code was returned.",
                                  assistance="Contact support for assistance",
                                  data=f"Raw response data: {response}")

    @staticmethod
    def determine_address_type(address: str) -> str:
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
                self.logger.info(f" Whitelist matched.  {address} was found in whitelist")
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

    def TypeFinder(self, host: str) -> str:
        """determines the type of host ipmask or fqdn"""
        type_ = "ipmask"
        try:
            host = ip_network(host)
        except ValueError:
            if re.match("^[0-9 .]+$", host):
                return type_
            elif host[-1].isdigit() or host[-2].isdigit():
                raise PluginException(cause="The host input appears to be an invalid IP or domain name.",
                                      assistance="Ensure that the host input is a valid IP or domain.",
                                      data=host)
            type_ = "fqdn"
            return type_
        return type_

    def ipmaskConverter(self, host: str) -> str:
        """Converts a IP or netmask into a CIDR"""
        try:
            host = ip_network(host)
        except ValueError:
            host = host.replace(" ", "/")
            host = ip_network(host)
        return str(host)

    def netmaskConverter(self, host: str) -> str:
        """Converts a CIDR or IP to a netmask"""
        host = IPv4Network(host).network_address
        host = str(host)
        host = host.replace("/", " ")
        return host

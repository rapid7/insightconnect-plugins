import insightconnect_plugin_runtime
from .schema import AddressInput, AddressOutput, Output, Input, Component

# Custom imports below
import socket
from insightconnect_plugin_runtime.exceptions import PluginException


class Address(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="address", description=Component.DESCRIPTION, input=AddressInput(), output=AddressOutput()
        )

    def ip_check(self, address):
        try:
            socket.inet_aton(address)
            return True
        except socket.error:
            self.logger.error("The IP address is invalid, please provide a valid IPv4 address")
            raise PluginException(
                cause=f"An invalid IPv4 address was provided: {address}.",
                assistance="Please update the action input to include a valid IPv4 address.",
            )

    def run(self, params={}):
        self.ip_check(params.get(Input.DOMAIN))
        data = self.connection.client.search_address(params.get(Input.DOMAIN))

        if not data or int(data["response_code"]) == 0:
            self.logger.info("ThreatCrowd API did not return any matches.")
            return {Output.FOUND: False}

        return {
            Output.DOMAINS: insightconnect_plugin_runtime.helper.clean_list(data["resolutions"]),
            Output.HASHES: insightconnect_plugin_runtime.helper.clean_list(data["hashes"]),
            Output.MALICIOUS: self.connection.client.verdict(data["votes"]),
            Output.PERMALINK: data["permalink"],
            Output.REFERENCES: insightconnect_plugin_runtime.helper.clean_list(data["references"]),
            Output.FOUND: True,
        }

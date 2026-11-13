import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import IpWhoisInput, IpWhoisOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class IpWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_whois",
            description=Component.DESCRIPTION,
            input=IpWhoisInput(),
            output=IpWhoisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip_address = params.get(Input.IP_ADDRESS)
        # END INPUT BINDING - DO NOT REMOVE

        ip_value, reason = validators.ip(ip_address)
        if reason:
            return outputs.not_looked_up(reason)
        result = self.connection.client.lookup("IP WHOIS", "GET", constants.PATH_IP_WHOIS, {"ip": ip_value})
        organization = outputs.get_path(result.data_dict, "organization", "name")
        return outputs.single(result, {Output.ORGANIZATION_NAME: outputs.to_str(organization)})

import insightconnect_plugin_runtime
from .schema import GetAllAgentsByIpInput, GetAllAgentsByIpOutput, Input, Output, Component

# Custom imports below
from ipaddress import ip_address as IPAddress
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean


class GetAllAgentsByIp(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_all_agents_by_ip",
            description=Component.DESCRIPTION,
            input=GetAllAgentsByIpInput(),
            output=GetAllAgentsByIpOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip_address = params.get(Input.IP_ADDRESS, "")
        next_cursor = params.get(Input.NEXT_CURSOR)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            IPAddress(ip_address)
        except ValueError:
            raise PluginException(
                cause=f"Invalid input IP address: '{ip_address}'",
                assistance="Please ensure that the input is a valid IPv4 or IPv6 address.",
            )

        agents, next_cursor = self.connection.api.get_agents_by_ip(ip_address, next_cursor)
        return clean({Output.AGENTS: agents, Output.NEXT_CURSOR: next_cursor})

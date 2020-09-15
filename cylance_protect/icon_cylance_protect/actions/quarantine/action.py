import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
from icon_cylance_protect.util.find_helpers import find_in_whitelist, find_agent_by_ip
import validators


class Quarantine(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='quarantine',
            description=Component.DESCRIPTION,
            input=QuarantineInput(),
            output=QuarantineOutput())

    def run(self, params={}):
        whitelist = params.get(Input.WHITELIST, None)
        agent = params.get(Input.AGENT)

        if validators.ipv4(agent):
            found_agent = find_agent_by_ip(self.connection, agent)
            if found_agent != agent:
                agent = found_agent
            else:
                raise PluginException(
                    cause="Agent not found.",
                    assistance=f"Unable to find an agent with IP: {agent},"
                               f" please ensure that the IP address is correct."
                )

        device_obj = self.connection.client.get_agent_details(agent)

        if whitelist:
            matches = find_in_whitelist(device_obj, whitelist)
            if matches:
                raise PluginException(
                    cause="Agent found in the whitelist.",
                    assistance=f"If you would like to block this host, remove {str(matches)[1:-1]} from the whitelist."
                )

        return {
            Output.LOCKDOWN_DETAILS: self.connection.client.device_lockdown(device_obj.get('id'))
        }

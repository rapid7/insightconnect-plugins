import komand
from .schema import AgentsFirewallLoggingInput, AgentsFirewallLoggingOutput, Input, Output, Component
# Custom imports below


class AgentsFirewallLogging(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_firewall_logging',
                description=Component.DESCRIPTION,
                input=AgentsFirewallLoggingInput(),
                output=AgentsFirewallLoggingOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action_with_data("firewall-logging", params.get(Input.FILTER, None), params.get(Input.DATA, None)).get("affected", 0)
        }

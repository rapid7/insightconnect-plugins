import komand
from .schema import AgentsFetchFirewallRulesInput, AgentsFetchFirewallRulesOutput, Input, Output, Component
# Custom imports below


class AgentsFetchFirewallRules(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_fetch_firewall_rules',
                description=Component.DESCRIPTION,
                input=AgentsFetchFirewallRulesInput(),
                output=AgentsFetchFirewallRulesOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action_with_data("fetch-firewall-rules", params.get(Input.FILTER, None), params.get(Input.DATA, None)).get("affected", 0)
        }

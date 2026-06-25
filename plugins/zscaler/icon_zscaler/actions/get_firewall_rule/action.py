import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetFirewallRuleInput, GetFirewallRuleOutput, Input, Output, Component

# Custom imports below


class GetFirewallRule(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_firewall_rule",
            description=Component.DESCRIPTION,
            input=GetFirewallRuleInput(),
            output=GetFirewallRuleOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        rule_id = params.get(Input.RULE_ID)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.zia_client.get_firewall_rule(rule_id)
        return {
            Output.RULE: result,
        }

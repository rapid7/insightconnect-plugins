import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CreateFirewallRuleInput, CreateFirewallRuleOutput, Input, Output, Component

# Custom imports below


class CreateFirewallRule(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_firewall_rule",
            description=Component.DESCRIPTION,
            input=CreateFirewallRuleInput(),
            output=CreateFirewallRuleOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        rule_data = params.get(Input.RULE_DATA)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.zia_client.create_firewall_rule(rule_data)
        return {
            Output.RULE: result,
        }

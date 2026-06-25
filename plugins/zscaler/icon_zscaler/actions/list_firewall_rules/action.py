import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import ListFirewallRulesInput, ListFirewallRulesOutput, Input, Output, Component

# Custom imports below
from icon_zscaler.util.helpers import clean_dict


class ListFirewallRules(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_firewall_rules",
            description=Component.DESCRIPTION,
            input=ListFirewallRulesInput(),
            output=ListFirewallRulesOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        next_link = params.get(Input.NEXT_LINK)
        search = params.get(Input.SEARCH)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.zia_client.list_firewall_rules(next_link or None)
        rules = result.get("rules", [])

        # Client-side filtering by name (ZIA API doesn't support server-side search)
        if search:
            rules = [r for r in rules if search.lower() in r.get("name", "").lower()]

        return clean_dict(
            {
                Output.RULES: rules,
                Output.NEXT_LINK: result.get("next_link", ""),
            }
        )

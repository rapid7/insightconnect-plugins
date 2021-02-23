import insightconnect_plugin_runtime

from .schema import GetFirewallInput, GetFirewallOutput, Input, Component


class GetFirewall(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_firewall", description=Component.DESCRIPTION, input=GetFirewallInput(), output=GetFirewallOutput()
        )

    def run(self, params={}):
        return self.connection.client.get_firewall(params.get(Input.FIREWALL))

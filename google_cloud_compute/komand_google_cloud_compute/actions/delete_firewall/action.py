import insightconnect_plugin_runtime


from .schema import DeleteFirewallInput, DeleteFirewallOutput, Input, Component


class DeleteFirewall(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_firewall",
            description=Component.DESCRIPTION,
            input=DeleteFirewallInput(),
            output=DeleteFirewallOutput(),
        )

    def run(self, params={}):
        return self.connection.client.delete_firewall(params.get(Input.FIREWALL))

import insightconnect_plugin_runtime

from .schema import ListFirewallsInput, ListFirewallsOutput, Input, Component


# Custom imports below


class ListFirewalls(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_firewalls",
            description=Component.DESCRIPTION,
            input=ListFirewallsInput(),
            output=ListFirewallsOutput(),
        )

    def run(self, params={}):
        return self.connection.client.list_firewalls(
            params.get(Input.FILTER), params.get(Input.MAXRESULTS), params.get(Input.ORDERBY)
        )

import insightconnect_plugin_runtime

from .schema import UpdateFirewallInput, UpdateFirewallOutput, Input, Component


# Custom imports below


class UpdateFirewall(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_firewall",
            description=Component.DESCRIPTION,
            input=UpdateFirewallInput(),
            output=UpdateFirewallOutput(),
        )

    def run(self, params={}):
        data = {"allowed": params.get(Input.ALLOWED)}

        if params.get(Input.NAME):
            data["name"] = params.get(Input.NAME)
        if params.get(Input.DESCRIPTION):
            data["description"] = params.get(Input.DESCRIPTION)
        if params.get(Input.NETWORK):
            data["network"] = params.get(Input.NETWORK)
        if params.get(Input.SOURCETAGS):
            data["sourceTags"] = params.get(Input.SOURCETAGS)
        if params.get(Input.SOURCERANGES):
            data["sourceRanges"] = params.get(Input.SOURCERANGES)
        if params.get(Input.TARGETTAGS):
            data["targetTags"] = params.get(Input.TARGETTAGS)

        return self.connection.client.update_firewall(params.get(Input.FIREWALL), data)

import insightconnect_plugin_runtime

from .schema import InsertFirewallInput, InsertFirewallOutput, Input, Component


class InsertFirewall(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="insert_firewall",
            description=Component.DESCRIPTION,
            input=InsertFirewallInput(),
            output=InsertFirewallOutput(),
        )

    def run(self, params={}):
        data = {"name": params.get(Input.NAME), "allowed": params.get(Input.ALLOWED)}

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

        return self.connection.client.insert_firewall(data)

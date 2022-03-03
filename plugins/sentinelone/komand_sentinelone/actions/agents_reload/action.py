import insightconnect_plugin_runtime
from .schema import AgentsReloadInput, AgentsReloadOutput, Input, Output, Component


class AgentsReload(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="agents_reload",
            description=Component.DESCRIPTION,
            input=AgentsReloadInput(),
            output=AgentsReloadOutput(),
        )

    def run(self, params={}):
        response = self.connection.agents_support_action("reload", params.get(Input.FILTER), params.get(Input.MODULE))

        affected = response.get("data", {}).get("affected", 0)

        return {Output.AFFECTED: affected}

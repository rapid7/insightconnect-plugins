import insightconnect_plugin_runtime
from .schema import AgentsReloadInput, AgentsReloadOutput, Input, Output, Component

# Custom imports below


class AgentsReload(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="agents_reload",
            description=Component.DESCRIPTION,
            input=AgentsReloadInput(),
            output=AgentsReloadOutput(),
        )

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.client.agents_support_action(
                "reload",
                {
                    "filter": params.get(Input.FILTER),
                    "data": {"module": params.get(Input.MODULE)},
                },
            )
            .get("data", {})
            .get("affected", 0)
        }

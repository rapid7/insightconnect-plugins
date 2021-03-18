import insightconnect_plugin_runtime
from .schema import AgentsActionInput, AgentsActionOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AgentsAction(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="agents_action",
            description=Component.DESCRIPTION,
            input=AgentsActionInput(),
            output=AgentsActionOutput(),
        )

    def run(self, params={}):
        agent_filter = params.get(Input.FILTER, "")
        action = params.get(Input.ACTION, None)
        if not action:
            raise PluginException(cause="No action given.", assistance="A valid agent action must be given to perform.")

        if action in ["decommission", "disconnect", "restart-machine", "shutdown", "uninstall"]:
            if "ids" not in agent_filter and "groupIds" not in agent_filter and "filterId" not in agent_filter:
                raise PluginException(
                    cause="Wrong filter parameter.",
                    assistance="One of the following filter arguments must be supplied - ids, groupIds or filterId.",
                )

        response = self.connection.agents_action(action, agent_filter)

        affected = response.get("data", {}).get("affected", 0)

        return {Output.AFFECTED: affected}

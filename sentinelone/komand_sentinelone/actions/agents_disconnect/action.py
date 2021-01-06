import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import AgentsDisconnectInput, AgentsDisconnectOutput, Input, Output, Component


class AgentsDisconnect(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_disconnect',
                description=Component.DESCRIPTION,
                input=AgentsDisconnectInput(),
                output=AgentsDisconnectOutput())

    def run(self, params={}):
        agent_filter = params.get(Input.FILTER, "")
        if "ids" not in agent_filter and "groupIds" not in agent_filter and "filterId" not in agent_filter:
            self.logger.error("One of the following filter arguments must be supplied - ids, groupIds, filterId")
            raise PluginException(
                cause="Wrong filter parameter",
                assistance="One of the following filter arguments must be supplied - ids, groupIds, filterId"
            )

        response = self.connection.agents_action("disconnect", agent_filter)

        affected = response.get("data", {}).get("affected", 0)

        return {
            Output.AFFECTED: affected
        }

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import AgentsDecommissionInput, AgentsDecommissionOutput, Input, Output, Component


class AgentsDecommission(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_decommission',
                description=Component.DESCRIPTION,
                input=AgentsDecommissionInput(),
                output=AgentsDecommissionOutput())

    def run(self, params={}):
        agent_filter = params.get(Input.FILTER, "")
        self.logger.info(agent_filter)
        if "ids" not in agent_filter and "groupIds" not in agent_filter and "filterId" not in agent_filter:
            raise PluginException(
                cause="Wrong filter parameter",
                assistance="One of the following filter arguments must be supplied - ids, groupIds, filterId"
            )

        response = self.connection.agents_action("decommission", agent_filter)

        affected = response.get("data", {}).get("affected", 0)

        return {
            Output.AFFECTED: affected
        }

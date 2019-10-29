import komand
from komand.exceptions import PluginException
from .schema import AgentsRestartInput, AgentsRestartOutput, Input, Output, Component


class AgentsRestart(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_restart',
                description=Component.DESCRIPTION,
                input=AgentsRestartInput(),
                output=AgentsRestartOutput())

    def run(self, params={}):
        agent_filter = params.get(Input.FILTER, None)
        if "ids" not in agent_filter and "groupIds" not in agent_filter and "filterId" not in agent_filter:
            self.logger.error("One of the following filter arguments must be supplied - ids, groupIds, filterId")
            raise PluginException(
                cause="Wrong filter parameter",
                assistance="One of the following filter arguments must be supplied - ids, groupIds, filterId"
            )

        return {
            Output.AFFECTED: self.connection.agents_action("restart-machine", agent_filter).get("affected", 0)
        }

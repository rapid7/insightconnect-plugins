import komand
from komand.exceptions import ConnectionTestException
from .schema import AgentsDecommissionInput, AgentsDecommissionOutput, Input, Output, Component


class AgentsDecommission(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_decommission',
                description=Component.DESCRIPTION,
                input=AgentsDecommissionInput(),
                output=AgentsDecommissionOutput())

    def run(self, params={}):
        agent_filter = params.get(Input.FILTER, None)
        if "ids" not in agent_filter and "groupIds" not in agent_filter and "filterId" not in agent_filter:
            self.logger.error("One of the following filter arguments must be supplied - ids, groupIds, filterId")
            raise ConnectionTestException(
                cause="One of the following filter arguments must be supplied - ids, groupIds, filterId"
            )

        return {
            Output.AFFECTED: self.connection.agents_action("decommission", agent_filter).get("affected", 0)
        }

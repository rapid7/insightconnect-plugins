import komand
from komand_sentinelone.util.exceptions import PluginException
from .schema import AgentsUninstallInput, AgentsUninstallOutput, Input, Output, Component


class AgentsUninstall(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_uninstall',
                description=Component.DESCRIPTION,
                input=AgentsUninstallInput(),
                output=AgentsUninstallOutput())

    def run(self, params={}):
        agent_filter = params.get(Input.FILTER, None)
        if "ids" not in agent_filter and "groupIds" not in agent_filter and "filterId" not in agent_filter:
            self.logger.error("One of the following filter arguments must be supplied - ids, groupIds, filterId")
            raise PluginException(
                cause="Wrong filter parameter",
                assistance="One of the following filter arguments must be supplied - ids, groupIds, filterId"
            )

        return {
            Output.AFFECTED: self.connection.agents_action("uninstall", agent_filter).get("affected", 0)
        }

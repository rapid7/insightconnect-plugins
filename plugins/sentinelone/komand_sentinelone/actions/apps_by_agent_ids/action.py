import insightconnect_plugin_runtime
from .schema import AppsByAgentIdsInput, AppsByAgentIdsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sentinelone.util.helper import clean, Helper


class AppsByAgentIds(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="apps_by_agent_ids",
            description=Component.DESCRIPTION,
            input=AppsByAgentIdsInput(),
            output=AppsByAgentIdsOutput(),
        )

    def run(self, params={}):
        ids = Helper.join_or_empty(params.get(Input.IDS, []))

        if not ids:
            raise PluginException(
                cause="Input validation error.",
                assistance="Please provide valid 'Agent IDs' input.",
            )
        return {Output.DATA: self.connection.client.apps_by_agent_ids(ids).get("data", [])}

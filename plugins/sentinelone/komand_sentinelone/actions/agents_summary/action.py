import insightconnect_plugin_runtime
from .schema import AgentsSummaryInput, AgentsSummaryOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sentinelone.util.helper import Helper


class AgentsSummary(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="agents_summary",
            description=Component.DESCRIPTION,
            input=AgentsSummaryInput(),
            output=AgentsSummaryOutput(),
        )

    def run(self, params={}):
        # This action is supported in API v2.1 but not 2.0
        if self.connection.api_version == "2.0":
            raise PluginException(
                cause="Endpoint not found.",
                assistance="This action is not supported in SentinelOne API v2.0. Verify that your SentinelOne console supports "
                "SentinelOne API v2.1 and try again.",
            )

        response = self.connection.agents_summary(
            Helper.join_or_empty(params.get(Input.SITE_IDS, [])),
            Helper.join_or_empty(params.get(Input.ACCOUNT_IDS, [])),
        )

        data = response.get("data", {})

        return {
            Output.DECOMMISSIONED: data.get("decommissioned", 0),
            Output.INFECTED: data.get("infected", 0),
            Output.OUT_OF_DATE: data.get("outOfDate", 0),
            Output.ONLINE: data.get("online", 0),
            Output.TOTAL: data.get("total", 0),
            Output.UP_TO_DATE: data.get("upToDate", 0),
        }

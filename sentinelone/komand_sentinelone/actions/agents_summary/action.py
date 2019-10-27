import komand
from .schema import AgentsSummaryInput, AgentsSummaryOutput, Input, Output, Component
from komand_sentinelone.util.helper import Helper


class AgentsSummary(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_summary',
                description=Component.DESCRIPTION,
                input=AgentsSummaryInput(),
                output=AgentsSummaryOutput())

    def run(self, params={}):
        response = self.connection.agents_summary(
            Helper.join_or_empty(params.get(Input.SITE_IDS, [])),
            Helper.join_or_empty(params.get(Input.ACCOUNT_IDS, [])),
        )

        return {
            Output.DECOMMISSIONED: response.get("decommissioned", 0),
            Output.INFECTED: response.get("infected", 0),
            Output.OUT_OF_DATE: response.get("outOfDate", 0),
            Output.ONLINE: response.get("online", 0),
            Output.TOTAL: response.get("total", 0),
            Output.UP_TO_DATE: response.get("upToDate", 0),
        }

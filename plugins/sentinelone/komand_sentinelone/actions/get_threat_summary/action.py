import insightconnect_plugin_runtime
from .schema import GetThreatSummaryInput, GetThreatSummaryOutput, Output, Component

# Custom imports below
from komand_sentinelone.util.helper import clean


class GetThreatSummary(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_threat_summary",
            description=Component.DESCRIPTION,
            input=GetThreatSummaryInput(),
            output=GetThreatSummaryOutput(),
        )

    def run(self, params={}):  # pylint: disable=unused-argument
        response = self.connection.client.get_threat_summary()

        return {
            Output.DATA: clean(response.get("data", [])),
            Output.PAGINATION: clean(response.get("pagination")),
            **clean({Output.ERRORS: response.get("errors")}),
        }

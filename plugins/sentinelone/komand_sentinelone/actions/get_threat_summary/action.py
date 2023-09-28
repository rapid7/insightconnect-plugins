import insightconnect_plugin_runtime
from .schema import GetThreatSummaryInput, GetThreatSummaryOutput, Output
from komand_sentinelone.util.helper import clean

# Custom imports below


class GetThreatSummary(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_threat_summary",
            description="Gets summary of all threats",
            input=GetThreatSummaryInput(),
            output=GetThreatSummaryOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.get_threat_summary()

        return {
            Output.DATA: clean(response.get("data", [])),
            Output.PAGINATION: clean(response.get("pagination")),
            **clean({Output.ERRORS: response.get("errors")}),
        }

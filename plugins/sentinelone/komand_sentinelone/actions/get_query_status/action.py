import insightconnect_plugin_runtime
from .schema import GetQueryStatusInput, GetQueryStatusOutput, Output, Component

# Custom imports below
from komand_sentinelone.util.helper import clean


class GetQueryStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_query_status",
            description=Component.DESCRIPTION,
            input=GetQueryStatusInput(),
            output=GetQueryStatusOutput(),
        )

    def run(self, params={}):
        return {Output.RESPONSE: clean(self.connection.client.get_query_status(params).get("data", {}))}

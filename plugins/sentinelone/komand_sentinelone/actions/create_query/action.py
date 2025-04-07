import insightconnect_plugin_runtime
from .schema import CreateQueryInput, CreateQueryOutput, Output, Component

# Custom imports below
from komand_sentinelone.util.helper import clean


class CreateQuery(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_query",
            description=Component.DESCRIPTION,
            input=CreateQueryInput(),
            output=CreateQueryOutput(),
        )

    def run(self, params={}):
        parameters = params.copy()
        limit = parameters.get("limit")
        if not limit or limit not in range(1, 20001):
            parameters["limit"] = 100
        return {Output.QUERYID: self.connection.client.create_query(clean(parameters)).get("data", {}).get("queryId")}

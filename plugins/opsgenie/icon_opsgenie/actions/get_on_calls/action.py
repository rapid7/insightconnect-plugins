import insightconnect_plugin_runtime
from .schema import GetOnCallsInput, GetOnCallsOutput, Input, Output, Component


class GetOnCalls(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_on_calls", description=Component.DESCRIPTION, input=GetOnCallsInput(), output=GetOnCallsOutput()
        )

    def run(self, params={}):
        response = self.connection.client.get_on_calls(
            params.get(Input.SCHEDULEIDENTIFIER),
            params.get(Input.SCHEDULEIDENTIFIERTYPE),
            params.get(Input.FLAT),
            params.get(Input.DATE),
        )

        return {
            Output.DATA: response.get("data"),
            Output.REQUESTID: response.get("requestId"),
            Output.ELAPSED_TIME: response.get("took"),
        }

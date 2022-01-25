import insightconnect_plugin_runtime
from .schema import GetOnCallsInput, GetOnCallsOutput, Input, Component


class GetOnCalls(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_on_calls", description=Component.DESCRIPTION, input=GetOnCallsInput(), output=GetOnCallsOutput()
        )

    def run(self, params={}):
        return self.connection.client.get_on_calls(
            params.get(Input.SCHEDULEIDENTIFIER),
            params.get(Input.SCHEDULEIDENTIFIERTYPE),
            params.get(Input.FLAT),
            params.get(Input.DATE),
        )

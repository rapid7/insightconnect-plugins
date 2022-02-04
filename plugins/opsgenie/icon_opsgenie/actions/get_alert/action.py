import insightconnect_plugin_runtime
from .schema import GetAlertInput, GetAlertOutput, Input, Output, Component


class GetAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert", description=Component.DESCRIPTION, input=GetAlertInput(), output=GetAlertOutput()
        )

    def run(self, params={}):
        response = self.connection.client.get_alert(params.get(Input.IDENTIFIER), params.get(Input.IDENTIFIERTYPE))
        return {
            Output.DATA: response.get("data"),
            Output.REQUESTID: response.get("requestId"),
            Output.ELAPSED_TIME: response.get("took"),
        }

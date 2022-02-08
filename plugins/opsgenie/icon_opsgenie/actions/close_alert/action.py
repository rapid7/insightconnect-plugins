import insightconnect_plugin_runtime
from .schema import CloseAlertInput, CloseAlertOutput, Input, Output, Component


class CloseAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_alert", description=Component.DESCRIPTION, input=CloseAlertInput(), output=CloseAlertOutput()
        )

    def run(self, params={}):
        data = {
            "user": params.get(Input.USER),
            "source": params.get(Input.SOURCE),
            "note": params.get(Input.NOTE),
        }
        response = self.connection.client.close_alert(
            params.get(Input.IDENTIFIER), params.get(Input.IDENTIFIERTYPE), data
        )
        return {
            Output.RESULT: response.get("result"),
            Output.REQUESTID: response.get("requestId"),
            Output.ELAPSED_TIME: response.get("took"),
        }

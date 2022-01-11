import insightconnect_plugin_runtime
from .schema import CloseAlertInput, CloseAlertOutput, Input, Component


class CloseAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_alert", description=Component.DESCRIPTION, input=CloseAlertInput(), output=CloseAlertOutput()
        )

    def run(self, params={}):
        data = {
            Input.USER: params.get(Input.USER),
            Input.SOURCE: params.get(Input.SOURCE),
            Input.NOTE: params.get(Input.NOTE),
        }

        return self.connection.client.close_alert(params.get(Input.IDENTIFIER), params.get(Input.IDENTIFIERTYPE), data)

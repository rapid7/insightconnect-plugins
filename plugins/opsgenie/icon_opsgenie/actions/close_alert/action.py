import insightconnect_plugin_runtime
from .schema import CloseAlertInput, CloseAlertOutput, Input, Output, Component


class CloseAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_alert", description=Component.DESCRIPTION, input=CloseAlertInput(), output=CloseAlertOutput()
        )

    def run(self, params={}):
        results = self.connection.client.close_alert(
            self.params.get(Input.IDENTIFIER), self.params.get(Input.IDENTIFIERTYPE)
        )

        return {
            Output.REQUESTID: results[Output.REQUESTID],
            Output.TOOK: results[Output.TOOK],
            Output.RESULT: results[Output.RESULT],
        }

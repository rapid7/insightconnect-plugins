import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CloseAlertInput, CloseAlertOutput, Input, Output, Component

# Custom imports below


class CloseAlert(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_alert", description=Component.DESCRIPTION, input=CloseAlertInput(), output=CloseAlertOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION

        # END INPUT BINDING - DO NOT REMOVE
        response = self.connection.api.close_alert(identifier=params.get(Input.IDENTIFIER))
        return {
            Output.RESULT: response.get("result"),
            Output.REQUESTID: response.get("requestId"),
            Output.ELAPSED_TIME: response.get("took"),
        }

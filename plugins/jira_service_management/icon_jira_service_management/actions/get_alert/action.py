import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetAlertInput, GetAlertOutput, Input, Output, Component

# Custom imports below


class GetAlert(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert", description=Component.DESCRIPTION, input=GetAlertInput(), output=GetAlertOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        identifier = params.get(Input.IDENTIFIER, "")
        # END INPUT BINDING - DO NOT REMOVE
        response = self.connection.api.get_alert(identifier=identifier)
        return {
            Output.DATA: response,
        }

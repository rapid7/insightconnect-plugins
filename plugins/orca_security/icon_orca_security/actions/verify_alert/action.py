import insightconnect_plugin_runtime
from .schema import VerifyAlertInput, VerifyAlertOutput, Input, Output, Component

# Custom imports below


class VerifyAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="verify_alert", description=Component.DESCRIPTION, input=VerifyAlertInput(), output=VerifyAlertOutput()
        )

    def run(self, params={}):
        return {
            Output.STATUS: self.connection.api.verify_alert(params.get(Input.ALERT_ID)).get("status"),
            Output.SUCCESS: True,
        }

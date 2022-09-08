import insightconnect_plugin_runtime
from .schema import UpdateAlertStatusInput, UpdateAlertStatusOutput, Input, Output, Component

# Custom imports below


class UpdateAlertStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_alert_status",
            description=Component.DESCRIPTION,
            input=UpdateAlertStatusInput(),
            output=UpdateAlertStatusOutput(),
        )

    def run(self, params={}):
        return {
            Output.RESPONSE: self.connection.api.update_alert_status(
                params.get(Input.ALERT_ID), params.get(Input.STATUS)
            ).get("data")
        }

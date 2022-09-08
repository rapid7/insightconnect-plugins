import insightconnect_plugin_runtime
from .schema import UpdateAlertSeverityInput, UpdateAlertSeverityOutput, Input, Output, Component

# Custom imports below


class UpdateAlertSeverity(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_alert_severity",
            description=Component.DESCRIPTION,
            input=UpdateAlertSeverityInput(),
            output=UpdateAlertSeverityOutput(),
        )

    def run(self, params={}):
        return {
            Output.RESPONSE: self.connection.api.update_alert_severity(
                params.get(Input.ALERT_ID),
                {"severity": params.get(Input.SEVERITY)},
            )
        }

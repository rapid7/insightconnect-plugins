import insightconnect_plugin_runtime
from .schema import GetAlertByIdInput, GetAlertByIdOutput, Input, Output, Component

# Custom imports below


class GetAlertById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert_by_id",
            description=Component.DESCRIPTION,
            input=GetAlertByIdInput(),
            output=GetAlertByIdOutput(),
        )

    def run(self, params={}):
        return {Output.ALERT: self.connection.api.get_alert_by_id(params.get(Input.ALERT_ID))}

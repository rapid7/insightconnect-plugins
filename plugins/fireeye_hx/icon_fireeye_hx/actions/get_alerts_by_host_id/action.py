import insightconnect_plugin_runtime
from .schema import GetAlertsByHostIdInput, GetAlertsByHostIdOutput, Input, Output, Component

# Custom imports below


class GetAlertsByHostId(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alerts_by_host_id",
            description=Component.DESCRIPTION,
            input=GetAlertsByHostIdInput(),
            output=GetAlertsByHostIdOutput(),
        )

    def run(self, params={}):
        return {
            Output.ALERTS: insightconnect_plugin_runtime.helper.clean(
                self.connection.api.get_alerts_by_host_id(
                    params.get(Input.HOST_ID), params.get(Input.OFFSET), params.get(Input.LIMIT)
                )
            )
        }

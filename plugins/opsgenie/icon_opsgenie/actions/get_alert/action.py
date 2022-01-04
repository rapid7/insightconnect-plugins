import insightconnect_plugin_runtime
from .schema import GetAlertInput, GetAlertOutput, Input, Component


class GetAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alert", description=Component.DESCRIPTION, input=GetAlertInput(), output=GetAlertOutput()
        )

    def run(self, params={}):
        return self.connection.client.get_alert(params.get(Input.IDENTIFIER), params.get(Input.IDENTIFIERTYPE))

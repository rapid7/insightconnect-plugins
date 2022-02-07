import insightconnect_plugin_runtime
from .schema import TakedownRequestInput, TakedownRequestOutput, Input, Output, Component

# Custom imports below


class TakedownRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="takedown_request",
            description=Component.DESCRIPTION,
            input=TakedownRequestInput(),
            output=TakedownRequestOutput(),
        )

    def run(self, params={}):
        self.connection.client.takedown_request(params.get(Input.ALERT_ID), params.get(Input.TARGET))
        return {Output.STATUS: True}

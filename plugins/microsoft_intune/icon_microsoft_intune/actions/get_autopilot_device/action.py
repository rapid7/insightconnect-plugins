import insightconnect_plugin_runtime
from .schema import GetAutopilotDeviceInput, GetAutopilotDeviceOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class GetAutopilotDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_autopilot_device",
            description=Component.DESCRIPTION,
            input=GetAutopilotDeviceInput(),
            output=GetAutopilotDeviceOutput(),
        )

    def run(self, params={}):
        return {Output.DEVICE: clean(self.connection.api.get_autopilot_device(params.get(Input.DEVICEID)))}

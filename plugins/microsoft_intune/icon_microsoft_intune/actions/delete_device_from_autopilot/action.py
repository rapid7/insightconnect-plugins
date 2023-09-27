import insightconnect_plugin_runtime
from .schema import DeleteDeviceFromAutopilotInput, DeleteDeviceFromAutopilotOutput, Input, Output, Component

# Custom imports below


class DeleteDeviceFromAutopilot(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_device_from_autopilot",
            description=Component.DESCRIPTION,
            input=DeleteDeviceFromAutopilotInput(),
            output=DeleteDeviceFromAutopilotOutput(),
        )

    def run(self, params={}):
        return {Output.SUCCESS: self.connection.api.delete_device_from_autopilot(params.get(Input.DEVICEID))}

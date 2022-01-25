import insightconnect_plugin_runtime
from .schema import DeleteDeviceInput, DeleteDeviceOutput, Input, Output, Component

# Custom imports below


class DeleteDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_device",
            description=Component.DESCRIPTION,
            input=DeleteDeviceInput(),
            output=DeleteDeviceOutput(),
        )

    def run(self, params={}):
        self.connection.automox_api.delete_device(params.get(Input.ORG_ID), params.get(Input.DEVICE_ID))

        return {Output.SUCCESS: True}

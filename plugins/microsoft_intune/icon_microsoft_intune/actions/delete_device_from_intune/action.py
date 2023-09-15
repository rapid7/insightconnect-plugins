import insightconnect_plugin_runtime
from .schema import DeleteDeviceFromIntuneInput, DeleteDeviceFromIntuneOutput, Input, Output, Component

# Custom imports below


class DeleteDeviceFromIntune(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_device_from_intune",
            description=Component.DESCRIPTION,
            input=DeleteDeviceFromIntuneInput(),
            output=DeleteDeviceFromIntuneOutput(),
        )

    def run(self, params={}):
        return {Output.SUCCESS: self.connection.api.delete_device_from_intune(params.get(Input.DEVICEID))}

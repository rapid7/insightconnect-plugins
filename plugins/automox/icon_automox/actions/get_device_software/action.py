import insightconnect_plugin_runtime
from .schema import GetDeviceSoftwareInput, GetDeviceSoftwareOutput, Input, Output, Component

# Custom imports below


class GetDeviceSoftware(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_device_software",
            description=Component.DESCRIPTION,
            input=GetDeviceSoftwareInput(),
            output=GetDeviceSoftwareOutput(),
        )

    def run(self, params={}):
        device_software = self.connection.automox_api.get_device_software(
            params.get(Input.ORG_ID), params.get(Input.DEVICE_ID)
        )
        return {Output.SOFTWARE: device_software}

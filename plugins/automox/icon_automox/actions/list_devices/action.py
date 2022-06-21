import insightconnect_plugin_runtime
from .schema import ListDevicesInput, ListDevicesOutput, Input, Output, Component

# Custom imports below


class ListDevices(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_devices", description=Component.DESCRIPTION, input=ListDevicesInput(), output=ListDevicesOutput()
        )

    def run(self, params={}):
        devices = self.connection.automox_api.get_devices(params.get(Input.ORG_ID), params.get(Input.GROUP_ID))
        self.logger.info(f"Returned {len(devices)} devices")

        return {Output.DEVICES: devices}

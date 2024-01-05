import insightconnect_plugin_runtime
from .schema import ListDevicesInput, ListDevicesOutput, Input, Output, Component


# Custom imports below


class ListDevices(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_devices", description=Component.DESCRIPTION, input=ListDevicesInput(), output=ListDevicesOutput()
        )

    def run(self, params={}):
        # Don't define optional inputs to avoid zero value
        group_id = None
        if params.get(Input.GROUP_ID):
            group_id = params.get(Input.GROUP_ID)

        devices = self.connection.automox_api.get_devices(params.get(Input.ORG_ID), group_id)
        self.logger.info(f"Returned {len(devices)} devices")

        return {Output.DEVICES: devices}

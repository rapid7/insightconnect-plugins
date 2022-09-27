import insightconnect_plugin_runtime
from .schema import LockMobileDevicesInput, LockMobileDevicesOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class LockMobileDevices(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lock_mobile_devices",
            description=Component.DESCRIPTION,
            input=LockMobileDevicesInput(),
            output=LockMobileDevicesOutput(),
        )

    def run(self, params={}):
        devices_id = params.get(Input.DEVICES_ID)
        response = self.connection.client.lock_mobile_devices(devices_id)
        return {Output.STATUS: response.status_code}

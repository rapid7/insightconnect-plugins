import insightconnect_plugin_runtime
from .schema import GetDevicesNameIdInput, GetDevicesNameIdOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetDevicesNameId(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_devices_name_id",
            description=Component.DESCRIPTION,
            input=GetDevicesNameIdInput(),
            output=GetDevicesNameIdOutput(),
        )

    def run(self, params={}):
        name = params.get(Input.NAME)
        response = self.connection.client.get_devices_name_id(name)
        return {Output.DEVICE_DETAIL: response.get("user", {}).get("links", {})}

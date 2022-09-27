import insightconnect_plugin_runtime
from .schema import GetDeviceGroupsInput, GetDeviceGroupsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetDeviceGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_device_groups",
            description=Component.DESCRIPTION,
            input=GetDeviceGroupsInput(),
            output=GetDeviceGroupsOutput(),
        )

    def run(self, params={}):
        device_id = params.get(Input.ID)
        response = self.connection.client.get_device_groups(device_id)
        return {Output.DEVICE_GROUPS: response.get("mobile_device", {}).get("mobile_device_groups", [])}

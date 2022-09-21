import json
import insightconnect_plugin_runtime
from .schema import GetUserLocationInput, GetUserLocationOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetUserLocation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_location",
            description=Component.DESCRIPTION,
            input=GetUserLocationInput(),
            output=GetUserLocationOutput(),
        )

    def run(self, params={}):
        device_id = params.get(Input.ID)
        response = self.connection.client.get_user_location(device_id)
        return {Output.USER_LOCATION_DETAIL: response.get("mobile_device", {}).get("location")}

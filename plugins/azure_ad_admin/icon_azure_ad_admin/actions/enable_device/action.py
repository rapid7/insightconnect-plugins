import insightconnect_plugin_runtime
from .schema import EnableDeviceInput, EnableDeviceOutput, Input, Output, Component

# Custom imports below
import requests
from icon_azure_ad_admin.util.api_utils import raise_for_status
from icon_azure_ad_admin.util.constants import Endpoint


class EnableDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enable_device",
            description=Component.DESCRIPTION,
            input=EnableDeviceInput(),
            output=EnableDeviceOutput(),
        )

    def run(self, params={}):
        response = requests.request(
            method="PATCH",
            url=Endpoint.DEVICE_ID.format(self.connection.tenant, device_id=params.get(Input.DEVICEID)),
            json={"accountEnabled": True},
            headers=self.connection.get_headers(self.connection.get_auth_token()),
        )
        raise_for_status(response)
        return {Output.SUCCESS: True}

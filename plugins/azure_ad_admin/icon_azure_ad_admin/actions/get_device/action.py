import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.helper import clean

from .schema import GetDeviceInput, GetDeviceOutput, Input, Output, Component

# Custom imports below
from ...util.api_utils import raise_for_status
from ...util.constants import Endpoint


class GetDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_device", description=Component.DESCRIPTION, input=GetDeviceInput(), output=GetDeviceOutput()
        )

    def run(self, params={}):
        response = requests.request(
            method="GET",
            url=Endpoint.DEVICE_ID.format(self.connection.tenant, device_id=params.get(Input.DEVICEID)),
            headers=self.connection.get_headers(self.connection.get_auth_token()),
        )
        raise_for_status(response)
        device = response.json()
        return {Output.DEVICE: clean(device)}

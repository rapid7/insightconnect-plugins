import komand
from .schema import GetDevicesNameIdInput, GetDevicesNameIdOutput, Input, Output, Component

# Custom imports below
from komand.exceptions import PluginException
import json


class GetDevicesNameId(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_devices_name_id',
                description=Component.DESCRIPTION,
                input=GetDevicesNameIdInput(),
                output=GetDevicesNameIdOutput())

    def run(self, params={}):
        base_url = self.connection.base_url
        name = params.get(Input.NAME)
        endpoint = f'/JSSResource/users/name/{name}'
        url = f'{base_url}/{endpoint}'

        result = self.connection.session.get(url, auth=self.connection.session.auth,
                                             headers=self.connection.session.headers)

        try:
            json_ = result.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=result.text)

        try:
            output = json_["user"].get("links")
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=json_)

        return {
            Output.DEVICE_DETAIL:  output
        }

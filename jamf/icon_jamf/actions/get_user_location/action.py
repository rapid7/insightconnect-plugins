import json
import komand
from .schema import GetUserLocationInput, GetUserLocationOutput, Input, Output, Component

# Custom imports below
from komand.exceptions import PluginException


class GetUserLocation(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_location',
                description=Component.DESCRIPTION,
                input=GetUserLocationInput(),
                output=GetUserLocationOutput())

    def run(self, params={}):
        base_url = self.connection.base_url
        device_id = params.get(Input.ID)
        endpoint = f'/JSSResource/mobiledevices/id/{device_id}'

        url = f'{base_url}/{endpoint}'
        result = self.connection.session.get(url)

        try:
            json_ = result.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=result.text)

        try:
            user_location_detail = json_["mobile_device"]["location"]
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=json_)

        return {
            Output.USER_LOCATION_DETAIL: user_location_detail
        }

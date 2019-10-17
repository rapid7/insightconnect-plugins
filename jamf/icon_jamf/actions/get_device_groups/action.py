import komand
from .schema import GetDeviceGroupsInput, GetDeviceGroupsOutput, Input, Output, Component

# Custom imports below
from komand.exceptions import PluginException
import json


class GetDeviceGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_device_groups',
                description=Component.DESCRIPTION,
                input=GetDeviceGroupsInput(),
                output=GetDeviceGroupsOutput())

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
            mobile_device_groups = json_["mobile_device"]["mobile_device_groups"]
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=json_)

        return {
            Output.DEVICE_GROUPS: mobile_device_groups
        }

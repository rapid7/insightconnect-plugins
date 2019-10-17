import komand
from .schema import GetGroupDetailInput, GetGroupDetailOutput, Input, Output, Component

# Custom imports below
from komand.exceptions import PluginException
import json


class GetGroupDetail(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_group_detail',
                description=Component.DESCRIPTION,
                input=GetGroupDetailInput(),
                output=GetGroupDetailOutput())

    def run(self, params={}):
        base_url = self.connection.base_url
        id_ = params.get(Input.ID)
        endpoint = f'/JSSResource/mobiledevicegroups/id/{id_}'
        url = f'{base_url}/{endpoint}'

        result = self.connection.session.get(url)

        try:
            json_ = result.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=result.text)

        return {
            Output.GROUP_DETAIL: json_
        }

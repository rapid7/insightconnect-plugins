import komand
from .schema import GetCiInput, GetCiOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class GetCi(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_ci',
                description=Component.DESCRIPTION,
                input=GetCiInput(),
                output=GetCiOutput())

    def run(self, params={}):
        url = f'{self.connection.table_url}{params.get(Input.TABLE)}/{params.get(Input.SYSTEM_ID)}'
        method = "get"

        response = self.connection.request.make_request(url, method)

        try:
            result = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        return {
            Output.SERVICENOW_CI: result
        }

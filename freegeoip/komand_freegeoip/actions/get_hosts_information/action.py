import komand
from .schema import GetHostsInformationInput, GetHostsInformationOutput, Input, Output, Component
from komand.exceptions import PluginException


# Custom imports below


class GetHostsInformation(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_hosts_information',
            description=Component.DESCRIPTION,
            input=GetHostsInformationInput(),
            output=GetHostsInformationOutput())

    def run(self, params={}):
        response = self.connection.client.get_hosts_information(
            params.get(Input.HOSTS),
            params.get(Input.LANGUAGE, 'en'),
            params.get(Input.SHOULD_RETURN_HOSTNAME, True),
            params.get(Input.SHOULD_RETURN_HOSTNAME, True)
        )
        if 'success' in response and response['success'] is False:
            raise PluginException(
                cause='Server Error',
                assistance=response['error']['info']
            )

        if response['continent_code'] is None:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        return {
            Output.INFORMATION: komand.helper.clean_dict(response)
        }

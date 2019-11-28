import komand
from .schema import CreateIncidentInput, CreateIncidentOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class CreateIncident(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_incident',
                description=Component.DESCRIPTION,
                input=CreateIncidentInput(),
                output=CreateIncidentOutput())

    def run(self, params={}):
        url = self.connection.incident_url
        payload = params.get(Input.CREATE_DATA)
        method = "post"

        response = self.connection.request.make_request(url, method, payload=payload)

        try:
            result = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        sys_id = result.get("sys_id", "")

        if sys_id is None:
            raise PluginException(cause=f'Error: create_incident failed - no system_id returned.',
                                  assistance=f'Response: {response.text}')

        return {
            Output.SYSTEM_ID: sys_id
        }

import insightconnect_plugin_runtime
from .schema import ReadIncidentInput, ReadIncidentOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class ReadIncident(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='read_incident',
                description=Component.DESCRIPTION,
                input=ReadIncidentInput(),
                output=ReadIncidentOutput())

    def run(self, params={}):
        url = f'{self.connection.incident_url}/{params.get(Input.SYSTEM_ID)}'
        method = "get"

        response = self.connection.request.make_request(url, method)

        fields = params.get(Input.FILTERING_FIELDS).split(",")
        filtered_incident = {}

        try:
            for field in fields:
                filtered_incident[field] = response["resource"]["result"].get(field, "")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        return {
            Output.FILTERED_INCIDENT: filtered_incident
        }

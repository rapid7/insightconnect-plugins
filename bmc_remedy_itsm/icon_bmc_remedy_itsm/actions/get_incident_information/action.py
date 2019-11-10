import komand
from .schema import GetIncidentInformationInput, GetIncidentInformationOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from icon_bmc_remedy_itsm.util import error_handling
import requests
import json
import urllib.parse


class GetIncidentInformation(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_incident_information',
            description=Component.DESCRIPTION,
            input=GetIncidentInformationInput(),
            output=GetIncidentInformationOutput())

    def run(self, params={}):
        handler = error_handling.ErrorHelper()
        incident_id = params.get(Input.INCIDENT_ID)
        get_incident_id_endpoint = f"api/arsys/v1/entry/HPD%3AHelp%20Desk/{incident_id}"

        url = urllib.parse.urljoin(self.connection.url, get_incident_id_endpoint)
        headers = self.connection.make_headers_and_refresh_token()

        self.logger.info(f"Attempting to retrieve: {url}")
        result = requests.get(url, headers=headers)
        handler.error_handling(result)

        try:
            incident = result.json()
        except json.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=e)

        return {Output.INCIDENT: komand.helper.clean(incident)}

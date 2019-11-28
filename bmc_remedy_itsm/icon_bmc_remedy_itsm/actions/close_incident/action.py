import komand
from .schema import CloseIncidentInput, CloseIncidentOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from icon_bmc_remedy_itsm.util import error_handling
import json
import requests
import urllib.parse


class CloseIncident(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='close_incident',
            description=Component.DESCRIPTION,
            input=CloseIncidentInput(),
            output=CloseIncidentOutput())

    def run(self, params={}):
        handler = error_handling.ErrorHelper()
        incident_id = params.get(Input.INCIDENT_ID)
        resolution_type = params.get(Input.RESOLUTION_TYPE)
        resolution_description = params.get(Input.RESOLUTION_DESCRIPTION)

        uri = f"api/arsys/v1/entry/HPD%3AIncidentInterface/{incident_id}|{incident_id}"
        url = urllib.parse.urljoin(self.connection.url, uri)
        headers = self.connection.make_headers_and_refresh_token()

        original_incident_response = requests.get(url, headers=headers)
        handler.error_handling(original_incident_response)

        try:
            original_incident = komand.helper.clean(original_incident_response.json())
        except json.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=e)

        original_incident.get("values")["z1D Action"] = "Modify"
        original_incident.get("values")["Status"] = resolution_type
        original_incident.get("values")["Resolution"] = resolution_description

        result = requests.put(url, headers=headers, json=original_incident)
        handler.error_handling(result)

        original_incident_response = requests.get(url, headers=headers)

        # If we made it this far, and this call fails, something really unexpected happened.
        if not original_incident_response.status_code == 200:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR,
                                  data=original_incident_response.text)

        try:
            original_incident = original_incident_response.json()
        except json.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=e)

        return {Output.INCIDENT: komand.helper.clean(original_incident)}

import komand
from .schema import AddIncidentWorkNoteInput, AddIncidentWorkNoteOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from icon_bmc_remedy_itsm.util import error_handling
import json
import requests
import urllib.parse


class AddIncidentWorkNote(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_incident_work_note',
                description=Component.DESCRIPTION,
                input=AddIncidentWorkNoteInput(),
                output=AddIncidentWorkNoteOutput())

    def run(self, params={}):
        handler = error_handling.ErrorHelper()
        incident_id = params.get(Input.INCIDENT_ID)
        work_note = params.get(Input.WORK_NOTE)

        uri = f"api/arsys/v1/entry/HPD%3AIncidentInterface/{incident_id}|{incident_id}"

        url = urllib.parse.urljoin(self.connection.url, uri)
        headers = self.connection.make_headers_and_refresh_token()

        try:
            original_incident_response = requests.get(url, headers=headers)
        except json.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=e)

        handler.error_handling(original_incident_response)

        original_incident = komand.helper.clean(original_incident_response.json())

        original_incident.get("values")["z1D Action"] = "Modify"
        original_incident.get("values")["z1D_WorklogDetails"] = work_note

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

import komand
from .schema import UpdateIncidentInput, UpdateIncidentOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from icon_bmc_remedy_itsm.util import error_handling
import requests
import json
import urllib.parse


class UpdateIncident(komand.Action):
    _CONVERSION_KEY = {"Status": "status", "Description": "incident_description", "Impact": "impact",
                       "Urgency": "urgency", "Assigned Group": "assigned_group"}

    def __init__(self):
        super(self.__class__, self).__init__(
            name='update_incident',
            description=Component.DESCRIPTION,
            input=UpdateIncidentInput(),
            output=UpdateIncidentOutput())

    def run(self, params={}):
        handler = error_handling.ErrorHelper()
        incident_id = params.pop(Input.INCIDENT_ID)
        uri = f"api/arsys/v1/entry/HPD%3AIncidentInterface/{incident_id}|{incident_id}"
        other_inputs = params.pop(Input.OTHER_INPUTS)

        url = urllib.parse.urljoin(self.connection.url, uri)
        headers = self.connection.make_headers_and_refresh_token()

        original_incident_response = requests.get(url, headers=headers)
        handler.error_handling(original_incident_response)

        try:
            original_incident = komand.helper.clean(original_incident_response.json())
        except json.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=e)

        values = dict()

        for key, value in self._CONVERSION_KEY.items():
            if params.get(value):
                values.update({key: params[value]})
        values.update(other_inputs)

        try:
            for key, value in values:
                original_incident.get("values")[key] = value
        except KeyError:
            raise PluginException(cause="One or more of the input keys is invalid.",
                                  assistance="Check that the input keys in 'Other Inputs' are all valid.",
                                  data=values)

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

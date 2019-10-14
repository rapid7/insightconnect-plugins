import komand
from .schema import UpdateIncidentInput, UpdateIncidentOutput, Input, Output, Component
# Custom imports below
import requests
import json
import urllib.parse
from komand.exceptions import PluginException


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
        incident_id = params.pop(Input.INCIDENT_ID)
        uri = f"api/arsys/v1/entry/HPD%3AIncidentInterface/{incident_id}|{incident_id}"
        other_inputs = params.pop(Input.OTHER_INPUTS)

        values = dict()

        for key, value in self._CONVERSION_KEY.items():
            if params.get(value):
                values.update({key: params[value]})
        values.update(other_inputs)

        payload = {"values": values}

        url = urllib.parse.urljoin(self.connection.url, uri)
        headers = self.connection.make_headers_and_refresh_token()

        result = requests.put(url, headers=headers, json=payload)

        if result.status_code == 400:
            raise PluginException(cause="A 400 error code was returned",
                                  assistance="The error code indicates that the JSON Token was invalid."
                                             " This is normally caused by an incorrect username or password")
        try:
            result.raise_for_status()
        except requests.HTTPError as e:
            raise PluginException(cause=f"An unexpected error code was returned. Status code was {result.status_code}",
                                  assistance="Please contact support with the status code and error information",
                                  data=e)

        get_incident_id_endpoint = f"api/arsys/v1/entry/HPD%3AHelp%20Desk/{incident_id}"

        url = urllib.parse.urljoin(self.connection.url, get_incident_id_endpoint)
        headers = self.connection.make_headers_and_refresh_token()

        result = requests.get(url, headers=headers)

        if result.status_code == 400:
            raise PluginException(cause="An HTTP 400 status code was returned.",
                                  assistance="This status code indicates that the JSON Token was invalid."
                                             " This is normally caused by an incorrect username or password.")
        try:
            result.raise_for_status()
        except requests.HTTPError as e:
            raise PluginException(cause=f"An unexpected status code was returned. Status code was {result.status_code}.",
                                  assistance="Please contact support with the status code and error information.",
                                  data=e)

        try:
            incident = result.json()
        except json.JSONDecodeError as e:
            raise PluginException(PluginException.Preset.INVALID_JSON,
                                  data=e)

        return {Output.INCIDENT: komand.helper.clean(incident)}

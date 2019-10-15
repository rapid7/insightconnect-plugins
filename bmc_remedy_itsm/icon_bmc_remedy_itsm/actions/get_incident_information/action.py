import komand
from .schema import GetIncidentInformationInput, GetIncidentInformationOutput, Input, Output, Component
# Custom imports below
import requests
import json
import urllib.parse
from komand.exceptions import PluginException


class GetIncidentInformation(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_incident_information',
            description=Component.DESCRIPTION,
            input=GetIncidentInformationInput(),
            output=GetIncidentInformationOutput())

    def run(self, params={}):
        incident_id = params.get(Input.INCIDENT_ID)
        get_incident_id_endpoint = f"api/arsys/v1/entry/HPD%3AHelp%20Desk/{incident_id}"

        url = urllib.parse.urljoin(self.connection.url, get_incident_id_endpoint)
        headers = self.connection.make_headers_and_refresh_token()

        self.logger.info(f"Attempting to retrieve: {url}")
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

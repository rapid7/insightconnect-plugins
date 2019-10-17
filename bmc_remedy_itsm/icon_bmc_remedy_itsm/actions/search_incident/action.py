import komand
from .schema import SearchIncidentInput, SearchIncidentOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import requests
import json
import urllib.parse


class SearchIncident(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_incident',
                description=Component.DESCRIPTION,
                input=SearchIncidentInput(),
                output=SearchIncidentOutput())

    def run(self, params={}):
        search = params.get(Input.SEARCH_PARAMETERS)
        uri = f"api/arsys/v1/entry/HPD%3AIncidentInterface/?q={search}"

        url = urllib.parse.urljoin(self.connection.url, uri)
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
        try:
            incident_list = incident["entries"]
        except KeyError:
            raise PluginException(cause='The response did not contain a correctly formatted list.',
                                  assistance="Please contact support with the status code and error information.",
                                  data=incident)

        return {Output.ENTRIES: komand.helper.clean(incident_list)}

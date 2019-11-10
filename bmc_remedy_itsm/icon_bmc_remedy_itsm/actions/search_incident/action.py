import komand
from .schema import SearchIncidentInput, SearchIncidentOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from icon_bmc_remedy_itsm.util import error_handling
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
        handler = error_handling.ErrorHelper()
        search = params.get(Input.SEARCH_PARAMETERS)
        uri = f"api/arsys/v1/entry/HPD%3AIncidentInterface/?q={search}"

        url = urllib.parse.urljoin(self.connection.url, uri)
        headers = self.connection.make_headers_and_refresh_token()

        result = requests.get(url, headers=headers)
        handler.error_handling(result)

        try:
            incident = result.json()
        except json.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=e)
        try:
            incident_list = incident["entries"]
        except KeyError:
            raise PluginException(cause='The response did not contain a correctly formatted list.',
                                  assistance="Please contact support with the status code and error information.",
                                  data=incident)

        return {Output.ENTRIES: komand.helper.clean(incident_list)}

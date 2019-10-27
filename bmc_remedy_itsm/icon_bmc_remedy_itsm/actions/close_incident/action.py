import komand
from .schema import CloseIncidentInput, CloseIncidentOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException
import urllib.parse


class CloseIncident(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='close_incident',
            description=Component.DESCRIPTION,
            input=CloseIncidentInput(),
            output=CloseIncidentOutput())

    def run(self, params={}):
        incident_id = params.get(Input.INCIDENT_ID)
        uri = f"api/arsys/v1/entry/HPD%3AIncidentInterface/{incident_id}|{incident_id}"
        resolution = {"values": {"Status": params.get(Input.RESOLUTION_TYPE),
                                 "Resolution": params.get(Input.RESOLUTION_DESCRIPTION)}}

        url = urllib.parse.urljoin(self.connection.url, uri)
        headers = self.connection.make_headers_and_refresh_token()

        result = requests.put(url, headers=headers, json=resolution)

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

        return {Output.SUCCESS: True}

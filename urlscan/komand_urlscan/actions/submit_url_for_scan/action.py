import komand
from .schema import SubmitUrlForScanInput, SubmitUrlForScanOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import requests
import json


class SubmitUrlForScan(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='submit_url_for_scan',
            description=Component.DESCRIPTION,
            input=SubmitUrlForScanInput(),
            output=SubmitUrlForScanOutput())

    def run(self, params=None):
        if params is None:
            params = {}
        body = {'url': params[Input.URL]}
        if params[Input.PUBLIC]:
            body['public'] = 'on'

        response = requests.post(f'{self.connection.server}/scan', headers=self.connection.headers, data=body)

        try:
            out = response.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(cause="Received an unexpected response from the Urlscan API. ",
                                  assistance=f"(non-JSON or no response was received). Response was: {response.text}")

        if 'uuid' in out:
            return {Output.SCAN_ID: out['uuid']}

        if 'status' in out:
            if out['status'] == 401:
                # {'message': "No API key supplied. Send the key using the 'API-Key' header", 'status': 401}
                raise PluginException(preset=PluginException.Preset.API_KEY)

        # {
        #  "message": "Missing URL properties",
        #  "description": "The URL supplied was not OK, please specify it including the protocol, host and path (e.g. http://example.com/bar)",
        #  "status": 400
        # }

        if ('message' in out) and ('description' in out):
            raise PluginException(cause=f"{out['message']}. ", assistance=f"{out['description']}.")

        raise PluginException(cause="Received an unexpected response from the Urlscan API. ",
                              assistance=f"If the problem persists, please contact support. Response was: {response.text}")

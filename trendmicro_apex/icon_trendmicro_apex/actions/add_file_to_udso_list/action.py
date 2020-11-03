import komand
from .schema import AddFileToUdsoListInput, AddFileToUdsoListOutput, Input, Output, Component
# Custom imports below
import json
import requests
from komand.exceptions import PluginException
from requests.exceptions import RequestException


class AddFileToUdsoList(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_file_to_udso_list',
                description=Component.DESCRIPTION,
                input=AddFileToUdsoListInput(),
                output=AddFileToUdsoListOutput())
        self.api_path = '/WebApp/API/SuspiciousObjectResource/FileUDSO'
        self.api_http_method = 'PUT'

    def run(self, params={}):
        payload_notes = ''
        user_notes = params.get(Input.DESCRIPTION)
        if user_notes:
            payload_notes = user_notes
        payload_scan_action = params.get(Input.SCAN_ACTION)
        payload_filename = params.get(Input.FILE).get('filename')
        payload_file_contents = params.get(Input.FILE).get('content')

        payload = {
            "file_name": payload_filename,
            "file_content_base64_string": payload_file_contents,
            "file_scan_action": payload_scan_action,
            "note": payload_notes
        }
        json_payload = json.dumps(payload)
        self.connection.create_jwt_token(self.api_path, self.api_http_method, json_payload)
        request_url = self.connection.url + self.api_path

        response = None
        try:
            response = requests.put(request_url, headers=self.connection.header_dict, data=json_payload, verify=False)
            response.raise_for_status()
            return {Output.SUCCESS: response is not None}
        except RequestException as rex:
            if response:
                self.logger.error(f"Received status code: {response.status_code}")
                self.logger.error(f"Response was: {response.text}")
            raise PluginException(assistance="Please verify the connection details and input data.",
                                  cause="Error processing the Apex request.",
                                  data=rex)

import insightconnect_plugin_runtime
from .schema import AddFileToUdsoListInput, AddFileToUdsoListOutput, Input, Output, Component

# Custom imports below
import json
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from requests.exceptions import RequestException


class AddFileToUdsoList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_file_to_udso_list",
            description=Component.DESCRIPTION,
            input=AddFileToUdsoListInput(),
            output=AddFileToUdsoListOutput(),
        )
        self.api_path = "/WebApp/API/SuspiciousObjectResource/FileUDSO"
        self.api_http_method = "PUT"

    def run(self, params={}):
        payload_notes = ""
        user_notes = params.get(Input.DESCRIPTION)
        if user_notes:
            payload_notes = user_notes
        payload_scan_action = params.get(Input.SCAN_ACTION)
        payload_filename = params.get(Input.FILE).get("filename")
        payload_file_contents = params.get(Input.FILE).get("content")

        payload = {
            "file_name": payload_filename,
            "file_content_base64_string": payload_file_contents,
            "file_scan_action": payload_scan_action,
            "note": payload_notes,
        }
        json_payload = json.dumps(payload)

        response = self.connection.api.execute(self.api_http_method, self.api_path, json_payload)

        return {Output.SUCCESS: response is not None}

import sys
import os

sys.path.append(os.path.abspath("../"))


from komand_proofpoint_tap.connection.connection import Connection
import json
import logging

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_proofpoint_tap.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.SERVICE_PRINCIPAL: {"secretKey": "44d88612-fea8-a8f3-6de8-2e1278abb02f"},
                Input.SECRET: {"secretKey": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"

            def json(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}

                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        threat_id = kwargs.get("params", {}).get("threatId")
        campaign_id = kwargs.get("params", {}).get("campaignId")
        include_campaign_forensics = kwargs.get("params", {}).get("includeCampaignForensics")
        if campaign_id and not threat_id:
            return MockResponse("campaign_id", 200)
        if threat_id and not campaign_id and include_campaign_forensics is True:
            return MockResponse("threat_id_and_include_campaign_forensic", 200)
        if threat_id and not campaign_id and include_campaign_forensics is False:
            return MockResponse("threat_id_without_include_campaign_forensic", 200)
        return MockResponse("error", 404)

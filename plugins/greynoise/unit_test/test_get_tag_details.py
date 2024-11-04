import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.get_tag_details import GetTagDetails
from greynoise import GreyNoise
import json
import logging


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_get(*args, **kwargs):
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/tag_details.json")
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)
    return json.loads(get_messages_from_user_payload)


class MockConnection:
    def __init__(self):
        self.server = "test_server"
        self.api_key = "test_api_key"
        self.user_agent = "test_user_agent"
        self.gn_client = GreyNoise(api_key=self.api_key, api_server=self.server, integration_name=self.user_agent)


class TestGetTagDetails(TestCase):
    @mock.patch("greynoise.GreyNoise.metadata", side_effect=mocked_requests_get)
    def test_get_tag_details(self, mock_get):
        log = logging.getLogger("Test")
        test_tag_details = GetTagDetails()
        test_tag_details.connection = MockConnection()
        test_tag_details.logger = log

        working_params = {"tag_name": "Test Tag Name"}
        results = test_tag_details.run(working_params)
        expected = {
            "id": "1234",
            "label": "label",
            "slug": "slug",
            "name": "Test Tag Name",
            "category": "activity",
            "intention": "malicious",
            "description": "description",
            "references": ["https://nvd.nist.gov/vuln/detail/CVE-2024-38289"],
            "recommend_block": True,
            "cves": ["CVE-2024-38289"],
            "created_at": "2024-09-12",
            "related_tags": [],
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)

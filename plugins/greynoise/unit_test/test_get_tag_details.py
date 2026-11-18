import json
import logging
import os
from unittest import TestCase, mock

from icon_greynoise.actions.get_tag_details import GetTagDetails

from util import MockConnection, read_file_to_string


def tags_response(*_args, **_kwargs):
    return json.loads(read_file_to_string(os.path.join(os.path.dirname(__file__), "payloads/tag_details.json")))


class TestGetTagDetails(TestCase):
    @mock.patch("greynoise.GreyNoise.tags", side_effect=tags_response)
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
            "related_tags": [
                {
                    "id": "da78f2eb-fe6b-4e84-913c-cdab4ff067c2",
                    "name": "Oracle WebLogic RCE CVE-2020-14882",
                    "intention": "malicious",
                    "category": "activity",
                    "slug": "oracle-weblogic-rce-cve-2020-14882",
                }
            ],
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
        self.assertEqual(mock_get.call_args.kwargs["name"], "Test Tag Name")

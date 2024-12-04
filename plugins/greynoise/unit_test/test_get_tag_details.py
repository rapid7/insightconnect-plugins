import logging
from unittest import TestCase, mock

from icon_greynoise.actions.get_tag_details import GetTagDetails

from util import MockConnection, mocked_requests_get


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

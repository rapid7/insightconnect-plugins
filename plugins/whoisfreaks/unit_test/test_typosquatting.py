import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.typosquatting import Typosquatting
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestTyposquatting(ActionTestCase):
    action_class = Typosquatting

    def test_keyword(self):
        body = {
            "status": True,
            "totalRecords": 250,
            "currentPage": 1,
            "totalPages": 3,
            "hasNextPage": True,
            "nextPageToken": "token-2",
            "domains": [{"domainName": "examp1e.com"}],
        }
        params = {"keyword": "example", "page_token": "token-1", "fetch_size": 50}
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session, "GET", "/v3.0/domain/typos", {"keyword": "example", "pageToken": "token-1", "fetch_size": 50}
        )
        self.assertTrue(output["has_next_page"])
        self.assertEqual("token-2", output["next_page_token"])
        self.assertEqual(250, output["total_records"])

    def test_pattern(self):
        _, session = self.run_action({"pattern": "example.com"}, MockResponse(200, {"domains": []}))
        self.assertEqual({"pattern": "example.com", "fetch_size": 100}, session.calls[-1]["params"])

    def test_requires_exactly_one_search(self):
        for params in ({}, {"keyword": "a", "pattern": "b"}):
            with self.subTest(params=params), self.assertRaises(PluginException):
                self.run_action(params)

import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.actions.search_incidents import SearchIncidents
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request
from unit_test.payload_stubs import STUB_SEARCH_INCIDENTS_PARAMETERS


@patch("requests.Session.request", side_effect=mock_request)
class TestSearchIncidents(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SearchIncidents())
        self.connection = self.action.connection

    @parameterized.expand(
        [
            ["text"],
        ]
    )
    def test_search_incidents(self, _mock_req, keyword):
        STUB_SEARCH_INCIDENTS_PARAMETERS["keyword"] = keyword
        actual = self.action.run(STUB_SEARCH_INCIDENTS_PARAMETERS)
        expected = {"data": "this is good"}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["bad text", "No incidents found."],
        ]
    )
    def test_search_incidents_fail(self, _mock_req, keyword, cause):
        with self.assertRaises(PluginException) as exception:
            STUB_SEARCH_INCIDENTS_PARAMETERS["keyword"] = keyword
            self.action.run(STUB_SEARCH_INCIDENTS_PARAMETERS)
        self.assertEqual(exception.exception.cause, cause)

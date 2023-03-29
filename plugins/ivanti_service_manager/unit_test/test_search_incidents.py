import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.actions.search_incidents import SearchIncidents
from icon_ivanti_service_manager.actions.search_incidents.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request


class TestSearchIncidents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {"good_text": "text", "bad_text": "bad text"}

    def setUp(self) -> None:
        self.action = Util.default_connector(SearchIncidents())
        self.connection = self.action.connection

    @patch("requests.Session.request", side_effect=mock_request)
    def test_search_incidents(self, _mock_req):
        actual = self.action.run(
            {
                Input.KEYWORD: self.params.get("good_text"),
            }
        )
        expected = {"data": "this is good"}
        self.assertEqual(actual, expected)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_search_incidents_fail(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {
                    Input.KEYWORD: self.params.get("bad_text"),
                }
            )
        cause = "No incidents found."
        self.assertEqual(exception.exception.cause, cause)

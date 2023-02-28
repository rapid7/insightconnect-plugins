import sys
import os
import json

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
        cls.params = {"object_type": "incident", "skip": 0, "good_text": "text", "bad_text": "bad text", "top": 1}

    def setUp(self) -> None:
        self.action = Util.default_connector(SearchIncidents())
        self.connection = self.action.connection

    @patch("requests.Session.request", side_effect=mock_request)
    def test_search_incidents(self, _mock_req):
        actual = self.action.run(
            {
                Input.OBJECT_TYPE: self.params.get("object_type"),
                Input.SKIP: self.params.get("skip"),
                Input.TEXT: self.params.get("good_text"),
                Input.TOP: self.params.get("top"),
            }
        )
        expected = {"data": "this is good"}
        self.assertEqual(actual, expected)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_search_incidents_fail(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {
                    Input.OBJECT_TYPE: self.params.get("object_type"),
                    Input.SKIP: self.params.get("skip"),
                    Input.TEXT: self.params.get("bad_text"),
                    Input.TOP: self.params.get("top"),
                }
            )
        cause = "No incidents found."
        self.assertEqual(exception.exception.cause, cause)

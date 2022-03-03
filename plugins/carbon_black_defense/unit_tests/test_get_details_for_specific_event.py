import sys
import os
from unittest import TestCase
from unittest.mock import patch
from komand_carbon_black_defense.actions.get_details_for_specific_event import GetDetailsForSpecificEvent
from komand_carbon_black_defense.actions.get_details_for_specific_event.schema import (
    Input as GetDetailsForSpecificEventSchemaInput,
)
from unit_tests.util import Util
from insightconnect_plugin_runtime.exceptions import PluginException

from unit_tests.mock import (
    mock_request,
)

sys.path.append(os.path.abspath("../tests/"))


class TestGetDetailsForSpecificEvent(TestCase):
    def setUp(self) -> None:
        self.connection, self.action = Util.default_connector(GetDetailsForSpecificEvent())

    # approach: test valid requests and error handling for common responses
    # test get details for specific event with valid input
    @patch("requests.request", side_effect=mock_request)
    def test_get_details_for_specific_event(self, _mock_req):
        actual = self.action.run(
            {
                GetDetailsForSpecificEventSchemaInput.EVENT_IDS: "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
            }
        )
        expected = {
            "eventinfo": {
                "results": [],
                "num_found": 0,
                "num_available": 0,
                "approximate_unaggregated": 0,
                "num_aggregated": 0,
                "contacted": 48,
                "completed": 48,
            },
            "success": True,
        }
        self.assertEqual(actual, expected)

    # test get details for specific event with invalid credentials
    @patch("requests.request", side_effect=mock_request)
    def test_get_details_for_specific_event_unauthorized(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.connection.host = "url_invalid"
            self.action.run(
                {
                    GetDetailsForSpecificEventSchemaInput.EVENT_IDS: "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                }
            )
        cause = "Either the organization key, API key, or connector ID configured in your connection is invalid."
        self.assertEqual(exception.exception.cause, cause)

    # test get details for specific event with an invalid org key
    @patch("requests.request", side_effect=mock_request)
    def test_get_details_for_specific_event_forbidden(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.connection.org_key = "org_key_forbidden"
            self.action.run(
                {
                    GetDetailsForSpecificEventSchemaInput.EVENT_IDS: "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                }
            )
        cause = (
            "Access to resource at url/api/investigate/v2/orgs/org_key_forbidden/enriched_events/detail_jobs is "
            "forbidden. The client has authenticated but does not have permission to perform the POST operation."
        )
        self.assertEqual(exception.exception.cause, cause)

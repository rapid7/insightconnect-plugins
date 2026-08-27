import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from jsonschema.validators import validate

from util import Util
from icon_sophos_central.actions.get_alerts import GetAlerts


@patch("requests.request", side_effect=Util.mock_request)
class TestGetAlerts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAlerts())

    @parameterized.expand(
        [
            [
                "all_pages_aggregated",
                Util.read_file_to_dict("inputs/get_alerts.json.inp"),
                Util.read_file_to_dict("expected/get_alerts.json.exp"),
            ],
        ]
    )
    def test_get_alerts(self, mock_request, test_name: str, input_params: dict, expected: dict) -> None:
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, self.action.output.schema)

    def test_get_alerts_sends_cursor_as_page_from_key(self, mock_request) -> None:
        self.action.run(Util.read_file_to_dict("inputs/get_alerts.json.inp"))

        second_call_params = mock_request.call_args_list[-1].kwargs["params"]
        self.assertEqual(second_call_params.get("pageFromKey"), "alertsKey")
        self.assertTrue(second_call_params.get("pageTotal"))

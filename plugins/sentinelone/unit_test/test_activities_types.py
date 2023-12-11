import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.activities_types import ActivitiesTypes
from komand_sentinelone.actions.activities_types.schema import ActivitiesTypesOutput

from util import Util
from parameterized import parameterized
from jsonschema import validate


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestActivitiesTypes(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ActivitiesTypes())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("expected/activities_types.json.exp"),
            ],
        ]
    )
    def test_activities_types(self, mock_request, test_name, expected):
        actual = self.action.run()
        self.assertEqual(expected, actual)
        validate(actual, ActivitiesTypesOutput.schema)

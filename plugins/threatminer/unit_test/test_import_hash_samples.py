import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Callable, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from mock import mock_request_200, mock_request_500, mock_request_503, mocked_request
from parameterized import parameterized
from utils import Util

from icon_threatminer.actions.import_hash_samples import ImportHashSamples
from icon_threatminer.actions.import_hash_samples.schema import Input, Output


class TestImportHashSamples(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ImportHashSamples())

    @parameterized.expand(
        [
            (
                {Input.QUERY: "02699626f388ed830012e5b787640e71c56d42d8"},
                {
                    "status_code": 200,
                    "status_message": "Results found.",
                    "results": [
                        {"value": "4c60f3f5cccdfad6137eb0a3218ec4caa3294b164c86dbda8922f1c9a75558fd"},
                        {"value": "2acf0cb8b4bd9f4ae4298cbe4e6ac0b4ab410a29fe1b0c0d1f23996c2d08269b"},
                    ],
                },
            ),
        ]
    )
    @patch("requests.request", side_effect=mock_request_200)
    def test_import_hash_samples(
        self, input_parameters: Dict[str, Any], expected: Dict[str, Any], mock_requests: MagicMock
    ) -> None:
        response = self.action.run(input_parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, {Output.RESPONSE: expected})
        mock_requests.assert_called()

    @parameterized.expand(
        [
            (
                mock_request_500,
                PluginException.causes[PluginException.Preset.SERVER_ERROR],
                PluginException.assistances[PluginException.Preset.SERVER_ERROR],
            ),
            (
                mock_request_503,
                PluginException.causes[PluginException.Preset.SERVICE_UNAVAILABLE],
                PluginException.assistances[PluginException.Preset.SERVICE_UNAVAILABLE],
            ),
        ]
    )
    def test_import_hash_samples_exception(self, mock_request: Callable, cause: str, assistance: str) -> None:
        mocked_request(mock_request, "request")
        with self.assertRaises(PluginException) as context:
            self.action.run({})
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)

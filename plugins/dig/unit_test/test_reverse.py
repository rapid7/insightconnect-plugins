import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_dig.actions.reverse import Reverse
from komand_dig.util.constants import Message
from parameterized import parameterized

from util import Util


@patch("insightconnect_plugin_runtime.helper.exec_command", side_effect=Util.mock_dig)
class TestReverse(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Reverse())

    @parameterized.expand(
        [
            [
                "reverse",
                Util.read_file_to_dict("inputs/reverse.json.inp"),
                Util.read_file_to_dict("expected/reverse.json.exp"),
            ],
            [
                "reverse_no_resolver",
                Util.read_file_to_dict("inputs/reverse_no_resolver.json.inp"),
                Util.read_file_to_dict("expected/reverse_no_resolver.json.exp"),
            ],
        ]
    )
    def test_reverse(
        self, _mock_request: MagicMock, _test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        Util.remove_unnecessary_keys(actual)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "reverse_bad_ip_address",
                Util.read_file_to_dict("inputs/reverse_bad_ip_address.json.inp"),
                Message.INVALID_IP_ADDRESS_CAUSE.format("Address"),
                Message.INVALID_IP_ADDRESS_ASSISTANCE,
            ],
            [
                "reverse_bad_resolver",
                Util.read_file_to_dict("inputs/reverse_bad_resolver.json.inp"),
                Message.INVALID_IP_ADDRESS_CAUSE.format("Resolver"),
                Message.INVALID_IP_ADDRESS_ASSISTANCE,
            ],
        ]
    )
    def test_error(
        self, _mock_request: MagicMock, _test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)

import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_dig.actions.forward import Forward
from komand_dig.util.constants import Message
from parameterized import parameterized

from util import Util


@patch("insightconnect_plugin_runtime.helper.exec_command", side_effect=Util.mock_dig)
class TestForward(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Forward())

    @parameterized.expand(
        [
            [
                "forward",
                Util.read_file_to_dict("inputs/forward.json.inp"),
                Util.read_file_to_dict("expected/forward.json.exp"),
                False,
            ],
            [
                "forward_no_resolver",
                Util.read_file_to_dict("inputs/forward_no_resolver.json.inp"),
                Util.read_file_to_dict("expected/forward_no_resolver.json.exp"),
                True,
            ],
        ]
    )
    def test_forward(
        self,
        _mock_request: MagicMock,
        _test_name: str,
        input_params: Dict[str, Any],
        expected: Dict[str, Any],
        remove_answers: bool,
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        Util.remove_unnecessary_keys(actual, remove_answers)
        self.assertEqual(actual.get("question"), expected.get("question"))
        self.assertEqual(actual.get("status"), expected.get("status"))

    @parameterized.expand(
        [
            [
                "forward_bad_resolver",
                Util.read_file_to_dict("inputs/forward_bad_resolver.json.inp"),
                Message.INVALID_IP_ADDRESS_CAUSE.format("Resolver"),
                Message.INVALID_IP_ADDRESS_ASSISTANCE,
            ],
            [
                "forward_bad_domain",
                Util.read_file_to_dict("inputs/forward_bad_domain.json.inp"),
                Message.INVALID_DOMAIN_CAUSE,
                Message.INVALID_DOMAIN_ASSISTANCE,
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

import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any

from icon_azure_blob_storage.actions.create_container import CreateContainer
from icon_azure_blob_storage.actions.create_container.schema import Input, Output
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestCreateContainer(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request: MagicMock) -> None:
        cls.action = Util.default_connector(CreateContainer())

    def test_create_container(self, mock_request: MagicMock) -> None:
        input_parameters = {Input.CONTAINER_NAME: "valid-container-name"}
        actual = self.action.run(input_parameters)
        self.assertEqual(
            actual,
            {
                Output.SUCCESS: True,
                Output.MESSAGE: "Container creation was successfully submitted.",
            },
        )

    @parameterized.expand(
        [
            [
                "invalid_characters",
                {Input.CONTAINER_NAME: "invalid_container_NAME"},
                "Invalid input parameters.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/create_container_invalid_characters.json.exp"),
            ],
            [
                "container_exists",
                {Input.CONTAINER_NAME: "existing-container-name"},
                "Request made conflicts with an existing resource.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/create_container_container_exists.json.exp"),
            ],
        ]
    )
    def test_create_container_raise_exception(
        self,
        mock_request: MagicMock,
        test_name: str,
        input_parameters: dict[str, Any],
        cause: str,
        assistance: str,
        data: dict[str, Any],
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)

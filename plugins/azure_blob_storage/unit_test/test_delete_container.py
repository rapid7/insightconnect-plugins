import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from util import Util
from parameterized import parameterized
from icon_azure_blob_storage.actions.delete_container import DeleteContainer
from icon_azure_blob_storage.actions.delete_container.schema import Input
from icon_azure_blob_storage.actions.delete_container.schema import Output


@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteContainer(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(DeleteContainer())

    def test_delete_container(self, mock_request):
        input_parameters = {Input.CONTAINER_NAME: "delete_container_name"}
        actual = self.action.run(input_parameters)
        self.assertEqual(
            actual, {Output.SUCCESS: True, Output.MESSAGE: "Container deletion was successfully submitted."}
        )

    @parameterized.expand(
        [
            [
                "invalid_characters",
                {Input.CONTAINER_NAME: "delete_invalid_container_NAME"},
                "Invalid input parameters.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/delete_container_invalid_characters.json.exp"),
            ],
            [
                "container_not_exist",
                {Input.CONTAINER_NAME: "not_existing_container_name"},
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/container_not_found.json.exp"),
            ],
        ]
    )
    def test_delete_container_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)

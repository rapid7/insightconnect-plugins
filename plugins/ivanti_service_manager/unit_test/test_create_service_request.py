import sys
import os
import json

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.actions.create_service_request import CreateServiceRequest
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request
from unit_test.payload_stubs import STUB_CREATE_SERVICE_REQUEST_PARAMETERS


@patch("requests.Session.request", side_effect=mock_request)
class TestCreateServiceRequest(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(CreateServiceRequest())
        self.connection = self.action.connection

    @parameterized.expand(
        [
            ["identifier"],
        ]
    )
    def test_create_service_request_success(self, mock_request, service_request_template):
        STUB_CREATE_SERVICE_REQUEST_PARAMETERS["service_request_template"] = service_request_template
        actual = self.action.run(
            STUB_CREATE_SERVICE_REQUEST_PARAMETERS
        )
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_create_service_request.json.resp"
                )
            )
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["identifier_not_unique", "Multiple service request templates found."],
            ["no_identifier","No service request templates found."],
        ]
    )
    def test_create_service_request_fail(self, mock_request, service_request_template, cause):
        STUB_CREATE_SERVICE_REQUEST_PARAMETERS["service_request_template"] = service_request_template
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                STUB_CREATE_SERVICE_REQUEST_PARAMETERS
            )
            self.assertEqual(exception.exception.cause, cause)


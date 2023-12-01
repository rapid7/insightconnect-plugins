import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_abnormal_security.actions.manage_threat import ManageThreat
from icon_abnormal_security.actions.manage_threat.schema import Input, ManageThreatInput, ManageThreatOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from unittest.mock import patch
from jsonschema import validate


class TestManageThreat(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ManageThreat())

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_threat_remediate(self, mock_post):
        test_input = {
            Input.ACTION: "remediate",
            Input.THREAT_ID: "a456b27b-6d7c-362a-efef-b22489d379e2",
        }
        validate(test_input, ManageThreatInput.schema)
        actual = self.action.run(test_input)

        expected = {
            "response": {
                "actionId": "c22b382a-89ff-461f-be34-eafa543b891c",
                "statusUrl": "https://api.abnormalplatform.com/v1/threats/a456b27b-6d7c-362a-efef-b22489d379e2/actions/c22b382a-89ff-461f-be34-eafa543b891c",
            }
        }
        self.assertEqual(actual, expected)
        validate(expected, ManageThreatOutput.schema)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_threat_unremediate(self, mock_post):
        test_input = {
            Input.ACTION: "unremediate",
            Input.THREAT_ID: "763ab210-6d8b-220c-89d3-10aa87524bba",
        }
        validate(test_input, ManageThreatInput.schema)
        actual = self.action.run(test_input)
        expected = {
            "response": {
                "actionId": "a33a212a-89ff-461f-be34-ea52aff44a73",
                "statusUrl": "https://api.abnormalplatform.com/v1/threats/763ab210-6d8b-220c-89d3-10aa87524bba/actions/a33a212a-89ff-461f-be34-ea52aff44a73",
            }
        }

        self.assertEqual(actual, expected)
        validate(expected, ManageThreatOutput.schema)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_threat_invalid_threat_id(self, mock_post):
        with self.assertRaises(PluginException) as e:
            test_input = {
                Input.ACTION: "remediate",
                Input.THREAT_ID: "53ca2899-d987-22aa-30a7-22aa987c4319",
            }
            validate(test_input, ManageThreatInput.schema)
            self.action.run(test_input)
        self.assertEqual(
            e.exception.cause,
            "Invalid or unreachable endpoint provided.",
        )
        self.assertEqual(
            e.exception.assistance,
            "Verify the URLs or endpoints in your configuration are correct.",
        )
        self.assertEqual(e.exception.data, 'Response was: {"message": "Threat action does not exist"}')

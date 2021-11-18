import sys
import os
from unittest import TestCase
from unittest.mock import patch
from icon_cybereason.actions.delete_registry_key import DeleteRegistryKey
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_cybereason.actions.delete_registry_key.schema import Input, Output
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))


class TestDeleteRegistryKey(TestCase):
    @classmethod
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests_session)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(DeleteRegistryKey())

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_delete_registry_key(self, mock_request):
        actual = self.action.run(
            {
                Input.INITIATOR_USER_NAME: "user@example.com",
                Input.MALOP_ID: "11.2189746432167327222",
                Input.SENSOR: "hostname",
            }
        )
        expected = {
            "response": {
                "malopId": "11.2189746432167327222",
                "remediationId": "5144cf82-94c4-49f8-82cd-9ce1fcbd6a23",
                "start": 1624819406074,
                "initiatingUser": "user@example.com",
                "statusLog": [],
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_delete_registry_key_bad_malop(self, mock_request):
        malop_id = "invalid_malop_id"

        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.INITIATOR_USER_NAME: "user@example.com",
                    Input.MALOP_ID: malop_id,
                    Input.SENSOR: "hostname",
                }
            )

        cause = "Unable to retrieve detailed Malop information for invalid_malop_id."
        assist = "Please ensure that provided Malop ID is valid and try again."

        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assist, context.exception.assistance)

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_delete_registry_key_bad_machine(self, mock_request):
        malop_id = "malop_without_machine"

        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.INITIATOR_USER_NAME: "user@example.com",
                    Input.MALOP_ID: malop_id,
                    Input.SENSOR: "hostname_not_in_malop",
                }
            )

        cause = "No targets found for this machine in the Malop provided."
        assist = f"No remediation targets for machine: sensor_guid, in the provided Malop."

        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assist, context.exception.assistance)

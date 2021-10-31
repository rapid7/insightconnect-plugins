import sys
import os
from unittest import TestCase
from unittest.mock import patch
from icon_cybereason.actions.remediate_items import RemediateItems
from icon_cybereason.actions.remediate_items.schema import Input, Output
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))


class TestRemediateItems(TestCase):
    @classmethod
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests_session)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(RemediateItems())

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_remediate_items(self, mock_request):
        actual = self.action.run(
            {
                Input.INITIATOR_USER_NAME: "user@example.com",
                Input.ACTIONS_BY_MACHINE: {
                    "1187140749.1198775089551518743": [
                        {"targetId": "-1187140749.4110133525793827174", "actionType": "KILL_PROCESS"}
                    ]
                },
                Input.MALOP_ID: "11.2189746432167327222",
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

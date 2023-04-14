import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_freshservice.actions.list_all_agents import ListAllAgents
from icon_freshservice.actions.list_all_agents.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestListAllAgents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListAllAgents())

    @parameterized.expand(Util.load_parameters("list_all_agents").get("parameters"))
    def test_list_all_agents(
        self, mock_request, name, email, mobile_phone_number, work_phone_number, state, active, expected
    ):
        actual = self.action.run(
            {
                Input.EMAIL: email,
                Input.MOBILEPHONENUMBER: mobile_phone_number,
                Input.WORKPHONENUMBER: work_phone_number,
                Input.STATE: state,
                Input.ACTIVE: active,
            }
        )
        self.assertEqual(actual, expected)

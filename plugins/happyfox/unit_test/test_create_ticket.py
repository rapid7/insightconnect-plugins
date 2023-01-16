import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_happyfox.actions.create_ticket import CreateTicket
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestCreateTicket(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateTicket())

    @parameterized.expand(Util.load_parameters("create_ticket").get("parameters"))
    def test_create_ticket(self, mock_request, name, inputs, expected):
        actual = self.action.run(inputs)
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("create_ticket_bad").get("parameters"))
    def test_create_ticket_bad(self, mock_request, name, inputs, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(inputs)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

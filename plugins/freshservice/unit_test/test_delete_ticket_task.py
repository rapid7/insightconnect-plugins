import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_freshservice.actions.delete_ticket_task import DeleteTicketTask
from icon_freshservice.actions.delete_ticket_task.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestDeleteTicketTask(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteTicketTask())

    @parameterized.expand(Util.load_parameters("delete_ticket_task").get("parameters"))
    def test_delete_ticket_task(self, mock_request, name, ticked_id, task_id, expected):
        actual = self.action.run({Input.TICKETID: ticked_id, Input.TASKID: task_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("delete_ticket_task_bad").get("parameters"))
    def test_delete_ticket_task_bad(self, mock_request, name, ticked_id, task_id, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.TICKETID: ticked_id, Input.TASKID: task_id})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_easyvista.actions.close_ticket import CloseTicket
from icon_easyvista.actions.close_ticket.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestCloseTicket(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CloseTicket())

    @parameterized.expand(Util.load_parameters("close_ticket").get("parameters"))
    def test_close_ticket(
        self, mock_request, name, rfc_number, catalog_guid, comment, delete_actions, end_date, status_guid, expected
    ):
        actual = self.action.run(
            {
                Input.RFC_NUMBER: rfc_number,
                Input.CATALOG_GUID: catalog_guid,
                Input.COMMENT: comment,
                Input.DELETE_ACTIONS: delete_actions,
                Input.END_DATE: end_date,
                Input.STATUS_GUID: status_guid,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("close_ticket_bad").get("parameters"))
    def test_close_ticket(
        self,
        mock_request,
        name,
        rfc_number,
        catalog_guid,
        comment,
        delete_actions,
        end_date,
        status_guid,
        cause,
        assistance,
    ):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.RFC_NUMBER: rfc_number,
                    Input.CATALOG_GUID: catalog_guid,
                    Input.COMMENT: comment,
                    Input.DELETE_ACTIONS: delete_actions,
                    Input.END_DATE: end_date,
                    Input.STATUS_GUID: status_guid,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)

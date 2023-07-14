import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_freshservice.actions.update_ticket import UpdateTicket
from icon_freshservice.actions.update_ticket.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestUpdateTicket(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateTicket())

    @parameterized.expand(Util.load_parameters("update_ticket").get("parameters"))
    def test_update_ticket(
        self,
        mock_request,
        name,
        ticket_id,
        subject,
        description,
        status,
        requester_name,
        requester_id,
        email,
        phone,
        priority,
        impact,
        urgency,
        ticket_type,
        responder_id,
        due_by,
        fr_due_by,
        group_id,
        source,
        attachments,
        tags,
        department_id,
        category,
        sub_category,
        item_category,
        assets,
        custom_fields,
        expected,
    ):
        actual = self.action.run(
            {
                Input.TICKETID: ticket_id,
                Input.SUBJECT: subject,
                Input.DESCRIPTION: description,
                Input.STATUS: status,
                Input.NAME: requester_name,
                Input.REQUESTERID: requester_id,
                Input.EMAIL: email,
                Input.PHONE: phone,
                Input.PRIORITY: priority,
                Input.IMPACT: impact,
                Input.URGENCY: urgency,
                Input.TYPE: ticket_type,
                Input.RESPONDERID: responder_id,
                Input.DUEBY: due_by,
                Input.FRDUEBY: fr_due_by,
                Input.GROUPID: group_id,
                Input.SOURCE: source,
                Input.ATTACHMENTS: attachments,
                Input.TAGS: tags,
                Input.DEPARTMENTID: department_id,
                Input.CATEGORY: category,
                Input.SUBCATEGORY: sub_category,
                Input.ITEMCATEGORY: item_category,
                Input.ASSETS: assets,
                Input.CUSTOMFIELDS: custom_fields,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("update_ticket_bad").get("parameters"))
    def test_update_ticket_bad(
        self,
        mock_request,
        name,
        ticket_id,
        subject,
        description,
        status,
        requester_name,
        requester_id,
        email,
        phone,
        priority,
        impact,
        urgency,
        ticket_type,
        responder_id,
        due_by,
        fr_due_by,
        group_id,
        source,
        attachments,
        tags,
        department_id,
        category,
        sub_category,
        item_category,
        assets,
        custom_fields,
        cause,
        assistance,
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.TICKETID: ticket_id,
                    Input.SUBJECT: subject,
                    Input.DESCRIPTION: description,
                    Input.STATUS: status,
                    Input.NAME: requester_name,
                    Input.REQUESTERID: requester_id,
                    Input.EMAIL: email,
                    Input.PHONE: phone,
                    Input.PRIORITY: priority,
                    Input.IMPACT: impact,
                    Input.URGENCY: urgency,
                    Input.TYPE: ticket_type,
                    Input.RESPONDERID: responder_id,
                    Input.DUEBY: due_by,
                    Input.FRDUEBY: fr_due_by,
                    Input.GROUPID: group_id,
                    Input.SOURCE: source,
                    Input.ATTACHMENTS: attachments,
                    Input.TAGS: tags,
                    Input.DEPARTMENTID: department_id,
                    Input.CATEGORY: category,
                    Input.SUBCATEGORY: sub_category,
                    Input.ITEMCATEGORY: item_category,
                    Input.ASSETS: assets,
                    Input.CUSTOMFIELDS: custom_fields,
                }
            )
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

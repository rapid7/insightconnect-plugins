import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_freshservice.actions.create_ticket import CreateTicket
from icon_freshservice.actions.create_ticket.schema import Input
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
    def test_create_ticket(
        self,
        mock_request,
        name,
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
        cc_emails,
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
                Input.CCEMAILS: cc_emails,
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

    @parameterized.expand(Util.load_parameters("create_ticket_bad").get("parameters"))
    def test_create_ticket_bad(
        self,
        mock_request,
        name,
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
        cc_emails,
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
                    Input.CCEMAILS: cc_emails,
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

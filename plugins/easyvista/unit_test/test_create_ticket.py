import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_easyvista.actions.create_ticket import CreateTicket
from icon_easyvista.actions.create_ticket.schema import Input
from util import Util
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
        catalog,
        asset_id,
        asset_name,
        asset_tag,
        ci_id,
        ci_asset_tag,
        ci_name,
        department_id,
        department_code,
        description,
        impact_id,
        external_reference,
        location_id,
        location_code,
        origin,
        parentrequest,
        phone,
        recipient_id,
        recipient_identification,
        recipient_mail,
        recipient_name,
        requestor_identification,
        requestor_mail,
        requestor_name,
        severity_id,
        submit_date,
        title,
        urgency_id,
        expected,
    ):
        actual = self.action.run(
            {
                Input.CATALOG: catalog,
                Input.ASSET_ID: asset_id,
                Input.ASSET_NAME: asset_name,
                Input.ASSET_TAG: asset_tag,
                Input.CI_ID: ci_id,
                Input.CI_ASSET_TAG: ci_asset_tag,
                Input.CI_NAME: ci_name,
                Input.DEPARTMENT_ID: department_id,
                Input.DEPARTMENT_CODE: department_code,
                Input.DESCRIPTION: description,
                Input.IMPACT_ID: impact_id,
                Input.EXTERNAL_REFERENCE: external_reference,
                Input.LOCATION_ID: location_id,
                Input.LOCATION_CODE: location_code,
                Input.ORIGIN: origin,
                Input.PARENTREQUEST: parentrequest,
                Input.PHONE: phone,
                Input.RECIPIENT_ID: recipient_id,
                Input.RECIPIENT_IDENTIFICATION: recipient_identification,
                Input.RECIPIENT_MAIL: recipient_mail,
                Input.RECIPIENT_NAME: recipient_name,
                Input.REQUESTOR_IDENTIFICATION: requestor_identification,
                Input.REQUESTOR_MAIL: requestor_mail,
                Input.REQUESTOR_NAME: requestor_name,
                Input.SEVERITY_ID: severity_id,
                Input.SUBMIT_DATE: submit_date,
                Input.TITLE: title,
                Input.URGENCY_ID: urgency_id,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("create_ticket_bad").get("parameters"))
    def test_create_ticket_bad(
        self,
        mock_request,
        name,
        catalog,
        asset_id,
        asset_name,
        asset_tag,
        ci_id,
        ci_asset_tag,
        ci_name,
        department_id,
        department_code,
        description,
        impact_id,
        external_reference,
        location_id,
        location_code,
        origin,
        parentrequest,
        phone,
        recipient_id,
        recipient_identification,
        recipient_mail,
        recipient_name,
        requestor_identification,
        requestor_mail,
        requestor_name,
        severity_id,
        submit_date,
        title,
        urgency_id,
        cause,
        assistance,
        data,
    ):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CATALOG: catalog,
                    Input.ASSET_ID: asset_id,
                    Input.ASSET_NAME: asset_name,
                    Input.ASSET_TAG: asset_tag,
                    Input.CI_ID: ci_id,
                    Input.CI_ASSET_TAG: ci_asset_tag,
                    Input.CI_NAME: ci_name,
                    Input.DEPARTMENT_ID: department_id,
                    Input.DEPARTMENT_CODE: department_code,
                    Input.DESCRIPTION: description,
                    Input.IMPACT_ID: impact_id,
                    Input.EXTERNAL_REFERENCE: external_reference,
                    Input.LOCATION_ID: location_id,
                    Input.LOCATION_CODE: location_code,
                    Input.ORIGIN: origin,
                    Input.PARENTREQUEST: parentrequest,
                    Input.PHONE: phone,
                    Input.RECIPIENT_ID: recipient_id,
                    Input.RECIPIENT_IDENTIFICATION: recipient_identification,
                    Input.RECIPIENT_MAIL: recipient_mail,
                    Input.RECIPIENT_NAME: recipient_name,
                    Input.REQUESTOR_IDENTIFICATION: requestor_identification,
                    Input.REQUESTOR_MAIL: requestor_mail,
                    Input.REQUESTOR_NAME: requestor_name,
                    Input.SEVERITY_ID: severity_id,
                    Input.SUBMIT_DATE: submit_date,
                    Input.TITLE: title,
                    Input.URGENCY_ID: urgency_id,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)

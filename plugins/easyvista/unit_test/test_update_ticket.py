import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_easyvista.actions.update_ticket import UpdateTicket
from icon_easyvista.actions.update_ticket.schema import Input
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
        rfc_number,
        analytical_charge_id,
        asset_id,
        asset_serial,
        asset_tag,
        ci,
        ci_id,
        ci_serial,
        comment,
        continuity_plan_id,
        description,
        external_reference,
        impact_id,
        known_problems_id,
        net_price_cur_id,
        origin_tool_id,
        owner_id,
        owning_group_id,
        release_id,
        rental_net_price_cur_id,
        request_origin_id,
        requestor_phone,
        root_cause_id,
        submit_date_ut,
        system_id,
        title,
        urgency_id,
        expected,
    ):
        actual = self.action.run(
            {
                Input.RFC_NUMBER: rfc_number,
                Input.ANALYTICAL_CHARGE_ID: analytical_charge_id,
                Input.ASSET_ID: asset_id,
                Input.ASSET_SERIAL: asset_serial,
                Input.ASSET_TAG: asset_tag,
                Input.CI: ci,
                Input.CI_ID: ci_id,
                Input.CI_SERIAL: ci_serial,
                Input.COMMENT: comment,
                Input.CONTINUITY_PLAN_ID: continuity_plan_id,
                Input.DESCRIPTION: description,
                Input.EXTERNAL_REFERENCE: external_reference,
                Input.IMPACT_ID: impact_id,
                Input.KNOWN_PROBLEMS_ID: known_problems_id,
                Input.NET_PRICE_CUR_ID: net_price_cur_id,
                Input.ORIGIN_TOOL_ID: origin_tool_id,
                Input.OWNER_ID: owner_id,
                Input.OWNING_GROUP_ID: owning_group_id,
                Input.RELEASE_ID: release_id,
                Input.RENTAL_NET_PRICE_CUR_ID: rental_net_price_cur_id,
                Input.REQUEST_ORIGIN_ID: request_origin_id,
                Input.REQUESTOR_PHONE: requestor_phone,
                Input.ROOT_CAUSE_ID: root_cause_id,
                Input.SUBMIT_DATE_UT: submit_date_ut,
                Input.SYSTEM_ID: system_id,
                Input.TITLE: title,
                Input.URGENCY_ID: urgency_id,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("update_ticket_bad").get("parameters"))
    def test_update_ticket_bad(
        self,
        mock_request,
        name,
        rfc_number,
        analytical_charge_id,
        asset_id,
        asset_serial,
        asset_tag,
        ci,
        ci_id,
        ci_serial,
        comment,
        continuity_plan_id,
        description,
        external_reference,
        impact_id,
        known_problems_id,
        net_price_cur_id,
        origin_tool_id,
        owner_id,
        owning_group_id,
        release_id,
        rental_net_price_cur_id,
        request_origin_id,
        requestor_phone,
        root_cause_id,
        submit_date_ut,
        system_id,
        title,
        urgency_id,
        cause,
        assistance,
        data,
    ):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.RFC_NUMBER: rfc_number,
                    Input.ANALYTICAL_CHARGE_ID: analytical_charge_id,
                    Input.ASSET_ID: asset_id,
                    Input.ASSET_SERIAL: asset_serial,
                    Input.ASSET_TAG: asset_tag,
                    Input.CI: ci,
                    Input.CI_ID: ci_id,
                    Input.CI_SERIAL: ci_serial,
                    Input.COMMENT: comment,
                    Input.CONTINUITY_PLAN_ID: continuity_plan_id,
                    Input.DESCRIPTION: description,
                    Input.EXTERNAL_REFERENCE: external_reference,
                    Input.IMPACT_ID: impact_id,
                    Input.KNOWN_PROBLEMS_ID: known_problems_id,
                    Input.NET_PRICE_CUR_ID: net_price_cur_id,
                    Input.ORIGIN_TOOL_ID: origin_tool_id,
                    Input.OWNER_ID: owner_id,
                    Input.OWNING_GROUP_ID: owning_group_id,
                    Input.RELEASE_ID: release_id,
                    Input.RENTAL_NET_PRICE_CUR_ID: rental_net_price_cur_id,
                    Input.REQUEST_ORIGIN_ID: request_origin_id,
                    Input.REQUESTOR_PHONE: requestor_phone,
                    Input.ROOT_CAUSE_ID: root_cause_id,
                    Input.SUBMIT_DATE_UT: submit_date_ut,
                    Input.SYSTEM_ID: system_id,
                    Input.TITLE: title,
                    Input.URGENCY_ID: urgency_id,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)

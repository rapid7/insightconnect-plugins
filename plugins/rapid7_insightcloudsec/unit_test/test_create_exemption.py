import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.actions.create_exemption import CreateExemption
from icon_rapid7_insightcloudsec.actions.create_exemption.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestCreateExemption(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateExemption())

    @parameterized.expand(Util.load_parameters("create_exemption").get("parameters"))
    def test_create_exemption(
        self,
        mock_request,
        name,
        approver,
        insight_id,
        insight_source,
        resource_ids,
        resource_type,
        start_date,
        expiration_date,
        notes,
        expected,
    ):
        actual = self.action.run(
            {
                Input.APPROVER: approver,
                Input.INSIGHTID: insight_id,
                Input.INSIGHTSOURCE: insight_source,
                Input.RESOURCEIDS: resource_ids,
                Input.RESOURCETYPE: resource_type,
                Input.STARTDATE: start_date,
                Input.EXPIRATIONDATE: expiration_date,
                Input.NOTES: notes,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("create_exemption_bad").get("parameters"))
    def test_create_exemption_bad(
        self,
        mock_request,
        name,
        approver,
        insight_id,
        insight_source,
        resource_ids,
        resource_type,
        start_date,
        expiration_date,
        notes,
        cause,
        assistance,
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.APPROVER: approver,
                    Input.INSIGHTID: insight_id,
                    Input.INSIGHTSOURCE: insight_source,
                    Input.RESOURCEIDS: resource_ids,
                    Input.RESOURCETYPE: resource_type,
                    Input.STARTDATE: start_date,
                    Input.EXPIRATIONDATE: expiration_date,
                    Input.NOTES: notes,
                }
            )
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

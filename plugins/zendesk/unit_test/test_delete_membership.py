import sys

sys.path.append("../")

from unittest import TestCase
from icon_zendesk.actions.delete_membership import DeleteMembership
from icon_zendesk.actions.delete_membership.schema import Input, Output
from unittest.mock import patch, Mock


from util import Util


class TestDeleteMemberships(TestCase):
    @classmethod
    @patch("zenpy.OrganizationMembershipApi.delete", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: Mock) -> None:
        cls.action = Util.default_connector(DeleteMembership())

    @patch("zenpy.OrganizationMembershipApi.delete", side_effect=Util.mocked_requests)
    @patch("zenpy.OrganizationMembershipApi.__call__", side_effect=Util.mocked_requests)
    def test_delete_membership(self, mock_request: Mock, mock_second: Mock) -> None:
        # happy path test- Note as of now- API just returns 204 and no actual response on success
        actual = self.action.run({Input.MEMBERSHIP_ID: 7})
        self.assertEqual(actual.get(Output.STATUS), True)

    @patch("zenpy.OrganizationMembershipApi.delete", side_effect=Util.mocked_requests)
    @patch("zenpy.OrganizationMembershipApi.__call__", side_effect=Util.mocked_requests)
    def test_delete_membership_fail(self, mock_request: Mock, mock_second: Mock) -> None:
        # Here -1 is showing an org id that doesn't exist. We don't expect an exception just a fail
        actual = self.action.run({Input.MEMBERSHIP_ID: -1})
        self.assertEqual(actual.get(Output.STATUS), False)

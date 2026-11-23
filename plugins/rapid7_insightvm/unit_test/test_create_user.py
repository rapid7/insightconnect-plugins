import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema.validators import validate
from komand_rapid7_insightvm.actions.create_user import CreateUser
from komand_rapid7_insightvm.actions.create_user.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestCreateUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateUser())

    @staticmethod
    def params(
        role_id: str = "Regular",
        email: str = "test.user@example.com",
        authentication_id: int = 4,
        access_all_sites: bool = False,
        access_all_asset_groups: bool = False,
    ) -> dict:
        return {
            Input.AUTHENTICATION_ID: authentication_id,
            Input.AUTHENTICATION_TYPE: "saml",
            Input.EMAIL: email,
            Input.ENABLED: True,
            Input.LOGIN: "test.user",
            Input.NAME: "Test User",
            Input.ROLE_ID: role_id,
            Input.ACCESS_ALL_ASSET_GROUPS: access_all_asset_groups,
            Input.ACCESS_ALL_SITES: access_all_sites,
        }

    @parameterized.expand(
        [
            # Role without privileges keeps every role flag false
            ["regular", "Regular", 4, {"type": "saml", "id": 4}, False, False, False, False, False],
            # All permissions grants every flag, superuser is required for global-admin only
            ["global_admin", "global-admin", 4, {"type": "saml", "id": 4}, False, False, True, True, True],
            # Manage sites grants access to all sites only
            ["site_admin", "site-admin", 4, {"type": "saml", "id": 4}, False, False, True, False, False],
            # Manage tags grants access to all sites only
            ["tag_admin", "tag-admin", 4, {"type": "saml", "id": 4}, False, False, True, False, False],
            # Manage dynamic asset groups grants access to all asset groups only
            ["asset_group_admin", "asset-group-admin", 4, {"type": "saml", "id": 4}, False, False, False, True, False],
            # Requested access is kept when the role has no privileges, so it must reach the payload
            ["requested_access", "Regular", 4, {"type": "saml", "id": 4}, True, True, True, True, False],
            # Default authentication ID of zero is invalid, so it is omitted
            ["no_authentication_id", "Regular", 0, {"type": "saml"}, False, False, False, False, False],
        ]
    )
    def test_create_user(
        self,
        mock_get,
        mock_post,
        name: str,
        role_id: str,
        authentication_id: int,
        expected_authentication: dict,
        access_all_sites: bool,
        access_all_asset_groups: bool,
        expected_all_sites: bool,
        expected_all_asset_groups: bool,
        expected_superuser: bool,
    ) -> None:
        actual = self.action.run(
            self.params(
                role_id=role_id,
                authentication_id=authentication_id,
                access_all_sites=access_all_sites,
                access_all_asset_groups=access_all_asset_groups,
            )
        )

        expected_payload = {
            "authentication": expected_authentication,
            "email": "test.user@example.com",
            "enabled": True,
            "login": "test.user",
            "name": "Test User",
            "role": {
                "allAssetGroups": expected_all_asset_groups,
                "allSites": expected_all_sites,
                "id": role_id,
                "superuser": expected_superuser,
            },
        }
        payload = mock_post.call_args.kwargs["json"]
        self.assertEqual(payload, expected_payload)

        # The console rejects null for its boolean role fields, and 0 or 1 would equal False or True above
        for flag in ("allAssetGroups", "allSites", "superuser"):
            self.assertIsInstance(payload["role"][flag], bool)

        self.assertEqual(actual, {"id": 807, "links": [{"href": "https://example.com/api/3/users/807", "rel": "self"}]})
        validate(actual, self.action.output.schema)

    def test_create_user_invalid_email(self, mock_get, mock_post) -> None:
        # This should fail with a PluginException
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params(email="not-an-email"))

        # Verify the exception data and that the user was not created
        self.assertEqual(context.exception.cause, "The email address for user account was not valid")
        self.assertEqual(context.exception.assistance, "Ensure that the email address is correct")
        mock_post.assert_not_called()

    def test_create_user_unknown_role(self, mock_get, mock_post) -> None:
        # This should fail with a PluginException
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params(role_id="missing-role"))

        # Verify the exception data and that the user was not created
        self.assertEqual(context.exception.cause, "InsightVM returned an error message. Not Found")
        self.assertEqual(context.exception.assistance, "Ensure that the requested resource exists.")
        self.assertEqual(context.exception.data, "The resource does not exist or access is prohibited.")
        mock_post.assert_not_called()

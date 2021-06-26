import sys
import os
import mock

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_microsoft_intune.actions.delete_app_from_policy import DeleteAppFromPolicy

from unit_test.utils import mocked_requests_request
from unit_test.utils import MockConnection


@mock.patch("requests.request", side_effect=mocked_requests_request)
class TestDeleteAppFromPolicy(TestCase):
    def test_delete_app_from_policy(self, mock_post):
        action = DeleteAppFromPolicy()
        action.connection = MockConnection()

        actual = action.run(
            {"application_name": "Comfy", "device_type": "android", "policy_name": "my-android-app-policy"}
        )
        expected = {"success": True}

        self.assertEqual(actual, expected)

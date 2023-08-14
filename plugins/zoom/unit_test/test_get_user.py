import os
import sys

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import MagicMock

from icon_zoom.actions.get_user import GetUser
from icon_zoom.actions.get_user.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from mock import STUB_USER_ID, Util, mock_request_201, mock_request_400, mock_request_404, mocked_request


class TestGetUser(TestCase):
    @mock.patch("requests.request", side_effect=mock_request_201)
    def setUp(self, mock_request) -> None:
        mocked_request(mock_request)
        self.action = Util.default_connector(GetUser())
        self.params = {Input.USER_ID: STUB_USER_ID}

    @mock.patch("icon_zoom.util.api.ZoomAPI.authenticate")
    @mock.patch("requests.request", side_effect=mock_request_201)
    def test_get_user_success(self, mock_get, mock_authenticate):
        mock_authenticate.return_value = 200
        response = self.action.run(self.params)
        expected_response = {
            "user": {
                "id": "zJKyaiAyTNC-MWjiWC18KQ",
                "dept": "Developers",
                "email": "jchill@example.com",
                "first_name": "Jill",
                "last_client_version": "5.9.6.4993(mac)",
                "last_login_time": "2021-05-05T20:40:30Z",
                "last_name": "Chill",
                "pmi": 3542471135,
                "role_name": "Admin",
                "timezone": "Asia/Shanghai",
                "type": 1,
                "use_pmi": False,
                "display_name": "Jill Chill",
                "account_id": "q6gBJVO5TzexKYTb_I2rpg",
                "account_number": 10009239,
                "cms_user_id": "KDcuGIm1QgePTO8WbOqwIQ",
                "company": "Jill",
                "user_created_at": "2018-10-31T04:32:37Z",
                "custom_attributes": {"key": "cbf_cywdkexrtqc73f97gd4w6g", "name": "A1", "value": "1"},
                "employee_unique_id": "HqDyI037Qjili1kNsSIrIg",
                "group_ids": ["RSMaSp8sTEGK0_oamiA2_w"],
                "im_group_ids": ["t-_-d56CSWG-7BF15LLrOw"],
                "jid": "jchill@example.com",
                "job_title": "API Developer",
                "language": "en-US",
                "location": "Paris",
                "login_types": [101],
                "manager": "thill@example.com",
                "personal_meeting_url": "example.com",
                "phone_numbers": [
                    {"code": "+1", "country": "US", "label": "Mobile", "number": "800000000", "verified": True}
                ],
                "pic_url": "example.com",
                "plan_united_type": "1",
                "pronouns": "3123",
                "pronouns_option": 1,
                "role_id": "0",
                "status": "pending",
                "vanity_url": "example.com",
                "verified": 1,
                "cluster": "us04",
                "zoom_one_type": 4,
            }
        }
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
        ],
    )
    @mock.patch("icon_zoom.util.api.ZoomAPI._refresh_oauth_token", return_value=None)
    def test_not_ok(self, mock_request: MagicMock, exception: str, mock_refresh: MagicMock) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)

import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_zoom.actions.create_user import CreateUser
from icon_zoom.actions.create_user.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.mock import (
    Util,
    STUB_CREATE_USER,
    mock_request_201,
    mock_request_400,
    mock_request_404,
    mocked_request,
)


class TestCreateUser(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_201)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(CreateUser())
        self.params = STUB_CREATE_USER

    def test_create_user_success(self):
        mocked_request(mock_request_201)
        response = self.action.run(self.params)
        expected_response = {
            "email": "jchill@example.com",
            "first_name": "Jill",
            "id": "KDcuGIm1QgePTO8WbOqwIQ",
            "last_name": "Chill",
            "type": 1,
        }

        self.assertEqual(response, expected_response)

    # @parameterized.expand(
    #     [
    #         (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
    #         (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
    #         (
    #             mock_request_409,
    #             "User already exists, try again.",
    #         ),
    #         (mock_request_429, PluginException.causes[PluginException.Preset.NOT_FOUND]),
    #     ],
    # )
    # # TODO - For 409, compare it to the something in the return
    # # TODO - For 429, we will have to check headers and see if whatever exists
    # def test_not_ok(self, mock_request, exception):
    #     mocked_request(mock_request)
    #
    #     with self.assertRaises(PluginException) as context:
    #         self.action.run(self.params)
    #     self.assertEqual(context.exception.cause, exception)

import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from komand_thehive.actions.create_case_task import CreateCaseTask
from insightconnect_plugin_runtime.exceptions import PluginException

from parameterized import parameterized
from unit_test.mock import (
    Util,
    mocked_request,
    mock_request_200,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_500,
)
from unit_test.constants import STUB_TASK


class TestCreateCaseTask(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(CreateCaseTask())
        self.params = STUB_TASK

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_create_case_task(self, mock_post):
        mocked_request(mock_post)
        response = self.action.run(self.params)
        expected = {
            "case": {
                "owner": "string",
                "_routing": "case_id",
                "flag": True,
                "dueDate": 1640000000000,
                "_type": "case_task",
                "description": "string",
                "title": "string",
                "createdAt": 1684244856627,
                "_parent": "case_id",
                "createdBy": "admin",
                "_id": "case_id",
                "id": "case_id",
                "_version": 1,
                "startDate": 1640000000000,
                "status": "Waiting",
                "group": "default",
                "order": 0,
            }
        }
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)

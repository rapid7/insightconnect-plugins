import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from komand_thehive.actions.get_case import GetCase
from komand_thehive.actions.get_case.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from parameterized import parameterized
from mock import (
    Util,
    mocked_request,
    mock_request_200,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_500,
)
from constants import STUB_CASE_ID


class TestGetCase(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(GetCase())
        self.params = {Input.ID: STUB_CASE_ID}

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_case(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run(self.params)
        expected = {
            "case": {
                "severity": 1,
                "owner": "admin",
                "_routing": "case_id",
                "flag": False,
                "customFields": {},
                "_type": "case",
                "description": "test",
                "title": "Test Case",
                "tags": [],
                "createdAt": 1683634850279,
                "_parent": None,
                "createdBy": "admin",
                "caseId": 23,
                "tlp": 0,
                "metrics": {},
                "_id": "case_id",
                "id": "case_id",
                "_version": 1,
                "pap": 0,
                "startDate": 1683634800000,
                "status": "Open",
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

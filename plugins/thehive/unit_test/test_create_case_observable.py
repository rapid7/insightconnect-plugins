import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from komand_thehive.actions.create_case_observable import CreateCaseObservable
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
from constants import STUB_OBSERVABLE


class TestCreateCaseObservable(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(CreateCaseObservable())
        self.params = STUB_OBSERVABLE

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_create_case_observable(self, mock_post):
        mocked_request(mock_post)
        response = self.action.run(self.params)
        expected = {
            "case": {
                "_routing": "case_id",
                "reports": {},
                "data": "string",
                "dataType": "domain",
                "_type": "case_artifact",
                "sighted": False,
                "message": "string",
                "tags": ["string"],
                "createdAt": 1684247621951,
                "_parent": "case_id",
                "createdBy": "admin",
                "tlp": 2,
                "_id": "random_id1234",
                "id": "random_id1234",
                "ioc": False,
                "_version": 1,
                "startDate": 1640000000000,
                "status": "Ok",
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

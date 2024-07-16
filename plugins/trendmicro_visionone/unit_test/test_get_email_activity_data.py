from unittest import TestCase
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import GetEmailActivityData
from mock import mock_connection, mock_params


class MockResponse:
    def __init__(self, total_count, result_code="", data=None):
        self.response = self
        self.total_count = total_count
        self.result_code = result_code
        self.data = data if data is not None else {}

    def model_dump(self):
        return self.data


class TestGetEmailActivityData(TestCase):
    def setUp(self):
        self.action = GetEmailActivityData()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("get_email_activity_data")

    def test_1_integration_get_email_activity_data(self):
        expected_result = self.mock_params["output"]

        # Mocking get_activity_count response
        mock_activity_count_response = MockResponse(total_count=100)
        self.action.connection.client.email.get_activity_count = MagicMock(return_value=mock_activity_count_response)

        # Mocking consume_activity response
        def consume_activity(callback, **kwargs):
            email_activity_data = MockResponse(total_count=100, result_code="success", data=expected_result)
            callback(email_activity_data.response)
            return MockResponse(total_count=100, result_code="success")

        self.action.connection.client.email.consume_activity = consume_activity

        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_2_get_email_activity_data_success(self):
        expected_result = self.mock_params["output"]

        # Mocking get_activity_count response
        mock_activity_count_response = MockResponse(total_count=100)
        self.action.connection.client.email.get_activity_count = MagicMock(return_value=mock_activity_count_response)

        # Mocking consume_activity response
        def consume_activity(callback, **kwargs):
            email_activity_data = MockResponse(total_count=100, result_code="success", data=expected_result)
            callback(email_activity_data.response)
            return MockResponse(total_count=100, result_code="success")

        self.action.connection.client.email.consume_activity = consume_activity

        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_3_get_email_activity_data_failure(self):
        self.action.connection.client.email.consume_activity = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])

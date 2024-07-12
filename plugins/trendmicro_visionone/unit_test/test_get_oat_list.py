from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import GetOatList
from mock import mock_connection, mock_params


class MockResponse:
    def __init__(self, total_count, result_code="", data=None):
        self.response = self
        self.total_count = total_count
        self.result_code = result_code
        self.data = data if data is not None else {}

    def model_dump_json(self):
        import json

        return json.dumps(self.data)


class TestGetOatList(TestCase):
    def setUp(self):
        self.action = GetOatList()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("get_oat_list")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_1_integration_get_oat_list(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_2_get_oat_list_success(self):
        expected_result = self.mock_params["output"]

        # Mocking oat.list response
        mock_list_response = MockResponse(total_count=10)
        self.action.connection.client.oat.list = MagicMock(return_value=mock_list_response)

        # Mocking oat.consume response
        def consume(callback, **kwargs):
            oat_data = MockResponse(total_count=10, result_code="success", data=expected_result)
            callback(oat_data)
            return MockResponse(total_count=10, result_code="success")

        self.action.connection.client.oat.consume = consume

        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_3_get_oat_list_failure(self):
        self.action.connection.client.oat.consume = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])

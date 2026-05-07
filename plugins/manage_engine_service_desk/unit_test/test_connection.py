import logging
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from icon_manage_engine_service_desk.connection.connection import Connection
from icon_manage_engine_service_desk.connection.schema import Input

VALID_ON_PREM_PARAMS = {
    Input.CONNECTION_TYPE: "On-Prem",
    Input.SDP_BASE_URL: "https://192.0.2.1:8080",
    Input.API_KEY: {"secretKey": "valid_api_key"},
    Input.SSL_VERIFY: False,
}

VALID_CLOUD_PARAMS = {
    Input.CONNECTION_TYPE: "Cloud",
    Input.CLIENT_ID: "client_id",
    Input.CLIENT_SECRET: {"secretKey": "client_secret"},
    Input.REFRESH_TOKEN: {"secretKey": "refresh_token"},
    Input.PORTAL_NAME: "mycompany",
    Input.DATA_CENTER: "United States",
}

MOCK_TOKEN_RESPONSE = {"access_token": "test_access_token", "expires_in": 3600}
MOCK_API_RESPONSE = {"requests": [], "response_status": [{"status": "success", "status_code": 2000}]}


class TestConnection(TestCase):
    def _make_connection(self):
        conn = Connection()
        conn.logger = logging.getLogger("test")
        conn.meta = "{}"
        return conn

    # --- _validate_on_prem_params ---

    def test_validate_on_prem_missing_url(self):
        with self.assertRaises(ConnectionTestException) as ctx:
            Connection._validate_on_prem_params({Input.API_KEY: {"secretKey": "key"}})
        self.assertIn("Service Desk Plus Base URL", ctx.exception.cause)

    def test_validate_on_prem_missing_api_key(self):
        with self.assertRaises(ConnectionTestException) as ctx:
            Connection._validate_on_prem_params({Input.SDP_BASE_URL: "https://192.0.2.1:8080"})
        self.assertIn("API Key", ctx.exception.cause)

    def test_validate_on_prem_missing_both(self):
        with self.assertRaises(ConnectionTestException) as ctx:
            Connection._validate_on_prem_params({})
        cause = ctx.exception.cause
        self.assertIn("Service Desk Plus Base URL", cause)
        self.assertIn("API Key", cause)

    def test_validate_on_prem_success(self):
        # Should not raise
        Connection._validate_on_prem_params(
            {Input.SDP_BASE_URL: "https://192.0.2.1:8080", Input.API_KEY: {"secretKey": "valid_key"}}
        )

    # --- _validate_cloud_params ---

    def test_validate_cloud_missing_all_fields(self):
        with self.assertRaises(ConnectionTestException) as ctx:
            Connection._validate_cloud_params({})
        cause = ctx.exception.cause
        for field in ["Client ID", "Client Secret", "Refresh Token", "Portal Name", "Data Center"]:
            self.assertIn(field, cause)

    def test_validate_cloud_missing_partial_fields(self):
        with self.assertRaises(ConnectionTestException) as ctx:
            Connection._validate_cloud_params({Input.CLIENT_ID: "client_id", Input.PORTAL_NAME: "mycompany"})
        cause = ctx.exception.cause
        self.assertNotIn("Client ID", cause)
        self.assertNotIn("Portal Name", cause)
        self.assertIn("Client Secret", cause)
        self.assertIn("Refresh Token", cause)
        self.assertIn("Data Center", cause)

    def test_validate_cloud_success(self):
        # Should not raise
        Connection._validate_cloud_params(
            {
                Input.CLIENT_ID: "client_id",
                Input.CLIENT_SECRET: {"secretKey": "client_secret"},
                Input.REFRESH_TOKEN: {"secretKey": "refresh_token"},
                Input.PORTAL_NAME: "mycompany",
                Input.DATA_CENTER: "United States",
            }
        )

    # --- connect() ---

    def test_connect_on_prem_creates_client(self):
        conn = self._make_connection()
        conn.connect(VALID_ON_PREM_PARAMS)
        self.assertIsNotNone(conn.api_client)

    def test_connect_cloud_creates_client(self):
        conn = self._make_connection()
        conn.connect(VALID_CLOUD_PARAMS)
        self.assertIsNotNone(conn.api_client)

    def test_connect_on_prem_missing_fields_raises(self):
        conn = self._make_connection()
        with self.assertRaises(ConnectionTestException):
            conn.connect({Input.CONNECTION_TYPE: "On-Prem"})

    def test_connect_cloud_missing_fields_raises(self):
        conn = self._make_connection()
        with self.assertRaises(ConnectionTestException):
            conn.connect({Input.CONNECTION_TYPE: "Cloud"})

    # --- test() ---

    @patch("requests.request")
    def test_test_on_prem_success(self, mock_request):
        mock_request.return_value = MagicMock(
            status_code=200,
            json=MagicMock(return_value=MOCK_API_RESPONSE),
        )
        conn = self._make_connection()
        conn.connect(VALID_ON_PREM_PARAMS)
        result = conn.test()
        self.assertEqual(result, {"status": "Success"})

    @patch("requests.post")
    @patch("requests.request")
    def test_test_cloud_success(self, mock_request, mock_post):
        mock_post.return_value = MagicMock(
            status_code=200,
            json=MagicMock(return_value=MOCK_TOKEN_RESPONSE),
            raise_for_status=MagicMock(),
        )
        mock_request.return_value = MagicMock(
            status_code=200,
            json=MagicMock(return_value=MOCK_API_RESPONSE),
        )
        conn = self._make_connection()
        conn.connect(VALID_CLOUD_PARAMS)
        result = conn.test()
        self.assertEqual(result, {"status": "Success"})

    @patch("requests.request")
    def test_test_raises_on_api_failure(self, mock_request):
        mock_request.return_value = MagicMock(
            status_code=403,
            json=MagicMock(return_value={"response_status": {"status_code": 4003, "status": "failed"}}),
        )
        conn = self._make_connection()
        conn.connect(VALID_ON_PREM_PARAMS)
        with self.assertRaises(ConnectionTestException):
            conn.test()

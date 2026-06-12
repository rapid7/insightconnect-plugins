import sys
import os

sys.path.append(os.path.abspath("../"))

import json
import pytest
from unittest.mock import patch, MagicMock
import requests

from komand_sentinelone_active_response.util.api import SentinelOneAPI
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import MockResponse


class TestSentinelOneAPI:
    def setup_method(self):
        self.api = SentinelOneAPI("https://test.sentinelone.net", "test_api_key", MagicMock())

    # --- test_connection tests ---

    @patch("requests.request")
    def test_test_connection_success(self, mock_request):
        mock_request.return_value = MockResponse(200, "auth_check_success.json")
        result = self.api.test_connection()
        assert "data" in result

    @patch("requests.request")
    def test_test_connection_auth_failure(self, mock_request):
        mock_request.return_value = MockResponse(401, "error_401.json")
        with pytest.raises(PluginException) as exc:
            self.api.test_connection()
        assert "Authentication failed" in exc.value.cause

    # --- search_agents tests ---

    @patch("requests.request")
    def test_search_agents_correct_url_and_params(self, mock_request):
        mock_request.return_value = MockResponse(200, "agent_single.json")
        self.api.search_agents({"computerName": "WORKSTATION-01"})
        mock_request.assert_called_once()
        call_args = mock_request.call_args
        url = call_args[0][1]
        assert "agents" in url
        assert "https://test.sentinelone.net/web/api/v2.1/agents" == url
        assert call_args[1]["params"] == {"computerName": "WORKSTATION-01"}

    # --- disconnect_agents and connect_agents tests ---

    @patch("requests.request")
    def test_disconnect_agents_correct_body(self, mock_request):
        mock_request.return_value = MockResponse(200, "disconnect_success.json")
        self.api.disconnect_agents(["123"])
        call_kwargs = mock_request.call_args[1]
        assert call_kwargs["json"] == {"filter": {"ids": ["123"]}}

    @patch("requests.request")
    def test_connect_agents_correct_body(self, mock_request):
        mock_request.return_value = MockResponse(200, "connect_success.json")
        self.api.connect_agents(["123"])
        call_kwargs = mock_request.call_args[1]
        assert call_kwargs["json"] == {"filter": {"ids": ["123"]}}

    # --- HTTP error mapping tests ---

    @patch("requests.request")
    def test_http_error_401(self, mock_request):
        mock_request.return_value = MockResponse(401, "error_401.json")
        with pytest.raises(PluginException) as exc:
            self.api.search_agents({})
        assert "Authentication failed" in exc.value.cause

    @patch("requests.request")
    def test_http_error_403(self, mock_request):
        mock_request.return_value = MockResponse(403, data={"error": "forbidden"})
        with pytest.raises(PluginException) as exc:
            self.api.search_agents({})
        assert "Forbidden" in exc.value.cause

    @patch("requests.request")
    def test_http_error_404(self, mock_request):
        mock_request.return_value = MockResponse(404, data={"error": "not found"})
        with pytest.raises(PluginException) as exc:
            self.api.search_agents({})
        assert "not found" in exc.value.cause.lower()

    @patch("requests.request")
    def test_http_error_429(self, mock_request):
        mock_request.return_value = MockResponse(429, "error_429.json")
        with pytest.raises(PluginException) as exc:
            self.api.search_agents({})
        assert "Rate limit" in exc.value.cause

    @patch("requests.request")
    def test_http_error_500(self, mock_request):
        mock_request.return_value = MockResponse(500, data={"error": "internal"})
        with pytest.raises(PluginException) as exc:
            self.api.search_agents({})
        assert "server error" in exc.value.cause.lower()

    @patch("requests.request")
    def test_http_error_503(self, mock_request):
        mock_request.return_value = MockResponse(503, data={"error": "unavailable"})
        with pytest.raises(PluginException) as exc:
            self.api.search_agents({})
        assert "unavailable" in exc.value.cause.lower()

    # --- Timeout and ConnectionError tests ---

    @patch("requests.request")
    def test_timeout_error(self, mock_request):
        mock_request.side_effect = requests.exceptions.Timeout("timeout")
        with pytest.raises(PluginException) as exc:
            self.api.search_agents({})
        assert "timed out" in exc.value.cause.lower()

    @patch("requests.request")
    def test_connection_error(self, mock_request):
        mock_request.side_effect = requests.exceptions.ConnectionError("connection refused")
        with pytest.raises(PluginException) as exc:
            self.api.search_agents({})
        assert "Unable to connect" in exc.value.cause
        assert "test.sentinelone.net" in exc.value.assistance

    # --- JSON decode failure test ---

    @patch("requests.request")
    def test_json_decode_error(self, mock_request):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.side_effect = json.JSONDecodeError("Expecting value", "doc", 0)
        mock_resp.text = "not json"
        mock_request.return_value = mock_resp
        with pytest.raises(PluginException) as exc:
            self.api.search_agents({})
        assert "unexpected response" in exc.value.cause.lower() or "parsed" in exc.value.assistance.lower()

    # --- get_agent_by_id tests ---

    @patch("requests.request")
    def test_get_agent_by_id_found(self, mock_request):
        mock_request.return_value = MockResponse(200, "agent_single.json")
        result = self.api.get_agent_by_id("1234567890123456789")
        assert result["id"] == "1234567890123456789"

    @patch("requests.request")
    def test_get_agent_by_id_not_found(self, mock_request):
        mock_request.return_value = MockResponse(200, data={"data": [], "pagination": {"totalItems": 0}})
        result = self.api.get_agent_by_id("nonexistent")
        assert result == {}

    # --- Authorization header test ---

    @patch("requests.request")
    def test_authorization_header(self, mock_request):
        mock_request.return_value = MockResponse(200, "auth_check_success.json")
        self.api.test_connection()
        call_kwargs = mock_request.call_args[1]
        assert call_kwargs["headers"]["Authorization"] == "APIToken test_api_key"

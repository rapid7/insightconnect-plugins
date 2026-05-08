import json
from logging import Logger
from typing import Optional

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .constants import API_VERSION, BASE_URL, FALLBACK_MODEL, HTTP_ERROR_MAP, MODEL_ERROR_INDICATORS, TIMEOUT


class AnthropicAPI:
    def __init__(self, api_key: str, model: str, logger: Logger):
        self.model = model
        self.logger = logger
        self.session = requests.Session()
        self.session.headers.update(
            {
                "x-api-key": api_key,
                "anthropic-version": API_VERSION,
                "content-type": "application/json",
            }
        )

    def test_connection(self) -> dict:
        """Test the API connection by counting tokens for a minimal message."""
        return self.count_tokens(prompt="test")

    def create_message(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 4096,
    ) -> dict:
        """Send a message to Claude and return the response. Falls back to a default model if the configured model is unavailable."""
        payload = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system_prompt:
            payload["system"] = system_prompt

        return self._make_request_with_model_fallback("POST", "/messages", json_data=payload)

    def count_tokens(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> dict:
        """Count tokens for a message without generating a response."""
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system_prompt:
            payload["system"] = system_prompt

        return self._make_request_with_model_fallback("POST", "/messages/count_tokens", json_data=payload)

    def _make_request_with_model_fallback(self, method: str, endpoint: str, json_data: Optional[dict] = None) -> dict:
        """Attempt a request with the configured model, falling back to the latest alias on model-related errors."""
        try:
            return self._make_request(method, endpoint, json_data=json_data)
        except PluginException as error:
            if self._is_model_error(error) and self.model != FALLBACK_MODEL:
                self.logger.warning(
                    f"Model '{self.model}' is unavailable or invalid. "
                    f"Falling back to '{FALLBACK_MODEL}'. "
                    f"Original error: {error.cause}"
                )
                json_data["model"] = FALLBACK_MODEL
                return self._make_request(method, endpoint, json_data=json_data)
            raise

    def _make_request(self, method: str, endpoint: str, json_data: Optional[dict] = None) -> dict:
        """Central method for making API requests."""
        url = f"{BASE_URL}{endpoint}"
        self.logger.info(f"Making {method} request to {endpoint}")

        try:
            response = self.session.request(
                method=method,
                url=url,
                json=json_data,
                timeout=TIMEOUT,
            )
        except requests.exceptions.Timeout:
            raise PluginException(preset=PluginException.Preset.TIMEOUT)
        except requests.exceptions.ConnectionError:
            raise PluginException(
                cause="Unable to connect to the Anthropic API.",
                assistance="Verify network connectivity and that https://api.anthropic.com is reachable.",
            )

        self._handle_status(response)
        return self._parse_response(response)

    def _handle_status(self, response: requests.Response) -> None:
        """Handle non-success HTTP status codes."""
        if 200 <= response.status_code < 300:
            return

        error_info = HTTP_ERROR_MAP.get(response.status_code)
        if error_info:
            raise PluginException(
                cause=error_info["cause"],
                assistance=error_info["assistance"],
                data=response.text,
            )

        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    @staticmethod
    def _is_model_error(error: PluginException) -> bool:
        """Determine if a PluginException is related to an invalid or unavailable model."""
        error_text = f"{error.cause or ''} {error.data or ''}".lower()
        return any(indicator in error_text for indicator in MODEL_ERROR_INDICATORS)

    @staticmethod
    def _parse_response(response: requests.Response) -> dict:
        """Parse JSON response with error handling."""
        try:
            return response.json()
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)

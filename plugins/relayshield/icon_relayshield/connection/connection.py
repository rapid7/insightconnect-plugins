import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

BASE_URL = "https://api.relayshield.net"


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.credentials = params.get(Input.CREDENTIALS)
        # END INPUT BINDING - DO NOT REMOVE
        self.api_key = self.credentials.get("secretKey", "")

    def test(self):
        try:
            resp = requests.post(
                f"{BASE_URL}/v1/metered/breach",
                json={"email": "connection-test@example.com"},
                headers={"X-RS-API-KEY": self.api_key, "Content-Type": "application/json"},
                timeout=15,
            )
        except requests.exceptions.RequestException as error:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVER_ERROR, data=str(error))

        if resp.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY, data=resp.text)
        if resp.status_code == 429:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.RATE_LIMIT, data=resp.text)
        if resp.status_code >= 500:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVER_ERROR, data=resp.text)
        if resp.status_code != 200:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN, data=resp.text)

        return resp.json()

    def call(self, path: str, payload: dict) -> dict:
        """Shared POST helper used by every action -- unwraps RelayShield's
        {"ok": true, "data": {...}} / {"ok": false, "error": "..."} envelope
        and raises PluginException on any non-2xx or ok:false response."""
        try:
            resp = requests.post(
                f"{BASE_URL}{path}",
                json=payload,
                headers={"X-RS-API-KEY": self.api_key, "Content-Type": "application/json"},
                timeout=30,
            )
        except requests.exceptions.RequestException as error:
            raise PluginException(
                cause=f"Request to RelayShield failed: {error}",
                assistance="Check network connectivity to api.relayshield.net and try again.",
            )

        try:
            body = resp.json()
        except ValueError:
            raise PluginException(
                cause=f"RelayShield returned a non-JSON response (HTTP {resp.status_code}).",
                assistance="This may indicate an upstream outage. Try again shortly.",
            )

        if resp.status_code == 401:
            raise PluginException(
                cause="RelayShield rejected the API key.",
                assistance="Verify the API key in this plugin's connection configuration.",
            )
        if not resp.ok or not body.get("ok", False):
            raise PluginException(
                cause=f"RelayShield API error: {body.get('error', 'unknown error')}",
                assistance="Check the input value and try again.",
            )

        return body.get("data", {})

import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
import json
import requests

DEFAULT_URL = "https://api.endoflife.ai"


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.base = None
        self.headers = None

    def connect(self, params):
        credentials = params.get(Input.API_KEY) or {}
        self.api_key = (credentials.get("secretKey") or "").strip() or None
        self.base = (params.get(Input.URL) or DEFAULT_URL).strip().rstrip("/")
        self.headers = {"Accept": "application/json", "User-Agent": "insightconnect-plugin-endoflife-ai/1.0.0"}
        if self.api_key:
            self.headers["X-API-Key"] = self.api_key
        self.logger.info(f"Connect: Connecting to {self.base}...")

    def test(self):
        url = f"{self.base}/v1"
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
        except requests.exceptions.RequestException as error:
            self.logger.error(error)
            raise ConnectionTestException(preset=PluginException.Preset.CONNECTION_ERROR, data=str(error))
        if response.status_code == 401 or response.status_code == 403:
            raise ConnectionTestException(preset=PluginException.Preset.API_KEY, data=response.text)
        if response.status_code == 429:
            raise ConnectionTestException(preset=PluginException.Preset.RATE_LIMIT, data=response.text)
        if response.status_code not in range(200, 299):
            raise ConnectionTestException(
                cause="Received an unexpected response from endoflife.ai.",
                assistance=f"(unexpected response was received). Response was: {response.text}; Status Code was: {response.status_code}",
            )
        try:
            json_ = response.json()
        except json.decoder.JSONDecodeError:
            raise ConnectionTestException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        if not isinstance(json_, dict) or "name" not in json_:
            raise ConnectionTestException(
                cause="The URL did not answer like the endoflife.ai API.",
                assistance="Verify the URL points at the endoflife.ai API root, for example https://api.endoflife.ai.",
                data=response.text,
            )
        # The index route answers without a key, and reports the caller's tier. Every action
        # needs a key (the API answers 401 without one), so a connection whose key is missing
        # or not recognised must fail here, not at the first action.
        if not self.api_key or json_.get("tier") in (None, "anon"):
            raise ConnectionTestException(
                cause="endoflife.ai did not recognise an API key on this connection.",
                assistance="Every action needs an API key. Add a key from https://endoflife.ai/api#free-key to the connection, or check the stored key for typing errors.",
                data=response.text,
            )
        return {"success": True, "tier": json_.get("tier"), "rate_limit": json_.get("rate_limit")}

import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
import requests
import base64


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.base_url = None
        self.api_key = None
        self.session = None

    def connect(self, params):
        self.logger.info("Connecting to Bitdefender GravityZone API...")

        # 1. Gather connection settings from the connection schema configuration
        # Base URL should look like: https://cloud.gravityzone.bitdefender.com or https://cloudgz.gravityzone.bitdefender.com
        self.base_url = params.get(Input.URL).rstrip("/")
        self.api_key = params.get(Input.API_KEY).get("secretKey")

        if not self.base_url.startswith("http"):
            raise PluginException(
                cause="Invalid Base URL configuration.",
                assistance="The URL scheme must start with http:// or https://"
            )

        # 2. Set up HTTP Basic Auth according to Bitdefender specs:
        # Username = API Key, Password = empty string -> "api_key:" encoded in base64
        login_string = f"{self.api_key}:"
        encoded_creds = base64.b64encode(login_string.encode("utf-8")).decode("utf-8")
        auth_header = f"Basic {encoded_creds}"

        # 3. Create a clean reusable requests session with persistent headers
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": auth_header,
            "Content-Type": "application/json"
        })

    def test(self):
        """
        InsightConnect calls test() to validate API credential health.
        We issue a lightweight, non-destructive licensing JSON-RPC call.
        """
        # Testing route directed at the licensing JSON-RPC module endpoint
        test_url = f"{self.base_url}/api/v1.0/jsonrpc/licensing"
        
        test_payload = {
            "jsonrpc": "2.0",
            "method": "getLicensingInfo",
            "params": {},
            "id": "insightconnect-health-check"
        }

        try:
            response = self.session.post(
                test_url,
                json=test_payload,
                verify=True,
                timeout=15
            )
            
            if response.status_code == 401 or response.status_code == 403:
                raise ConnectionTestException(
                    cause="Authentication failed.",
                    assistance="Please verify that your generated Bitdefender API Key is valid and active."
                )
                
            response.raise_for_status()
            response_json = response.json()

        except requests.exceptions.RequestException as e:
            raise ConnectionTestException(
                cause="Could not connect to Bitdefender GravityZone platform.",
                assistance=f"Please verify that the host URL: {self.base_url} is fully operational and reachable.",
                data=str(e)
            )

        # Handle explicit logical error blocks returned by Bitdefender's framework wrapper
        if "error" in response_json:
            error_msg = response_json.get("error", {}).get("message", "Unknown API internal error.")
            raise ConnectionTestException(
                cause=f"Bitdefender API rejected the request. Details: {error_msg}",
                assistance="Ensure your API token has standard permissions toggled on for the specified API services."
            )

        return {"success": True}
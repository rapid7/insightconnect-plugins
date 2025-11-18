import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_zscaler.util.api import ZscalerAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = ZscalerAPI(
            params.get(Input.URL).strip().strip("/").replace("/api/v1", ""),
            params.get(Input.API_KEY).get("secretKey"),
            params.get(Input.CREDENTIALS).get("username"),
            params.get(Input.CREDENTIALS).get("password"),
            self.logger,
        )

    def test(self):
        """
        Test the connection to the Zscaler API by calling the /v1/status endpoint.
        Validate that the response contains the expected 'status' field.
        :raises ConnectionTestException: If the connection test fails due to invalid response or other issues
        """
        try:
            get_status_resp = self.client.get_status()

            if not get_status_resp.content:
                self._raise_invalid_response("Empty response from Zscaler API")

            try:
                status = get_status_resp.json().get("status")
                if status is None:
                    self._raise_invalid_response("Missing 'status' field in Zscaler API response")
            except ValueError:
                self._raise_invalid_response("Invalid JSON response from Zscaler API")

            return {"success": True}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)

    def _raise_invalid_response(self, message):
        raise ConnectionTestException(
            cause=PluginException.causes[PluginException.Preset.INVALID_JSON],
            assistance=PluginException.assistances[PluginException.Preset.SERVER_ERROR],
            data=message,
        )

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from komand_mimecast.util.exceptions import ApiClientException
from komand_mimecast.util.api import MimecastAPI
from .schema import ConnectionSchema, Input
from komand_mimecast.util.constants import API, META_FIELD, FAIL_FIELD, STATUS_FIELD


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.access_key = None
        self.secret_key = None
        self.app_key = None
        self.app_id = None
        self.url = None

    def connect(self, params={}):
        self.client = MimecastAPI(
            params.get(Input.CLIENT_ID, "").strip(),
            params.get(Input.CLIENT_SECRET, {}).get("secretKey", "").strip(),
            self.logger,
        )
        self.client.authenticate()

    def test(self):
        # pylint: disable=protected-access
        response = self.client._handle_rest_call("POST", f"{API}/account/get-account")
        if response.get(META_FIELD, {}).get(STATUS_FIELD) != 200 or response.get(FAIL_FIELD) != []:
            self.logger.error(response)
            raise ConnectionTestException(
                cause="Server request failed.",
                assistance=f"Status code is {response.get(META_FIELD, {}).get(STATUS_FIELD)}, see log for details.",
                data=response.get(FAIL_FIELD),
            )
        return {"success": True}

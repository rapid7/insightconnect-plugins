import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from komand_mimecast.util import util
from komand_mimecast.util.api import MimecastAPI
from .schema import ConnectionSchema, Input
from komand_mimecast.util.constants import DEFAULT_REGION, API, META_FIELD, FAIL_FIELD, STATUS_FIELD


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
            params.get(Input.REGION, DEFAULT_REGION),
            params.get(Input.ACCESS_KEY).get("secretKey"),
            params.get(Input.SECRET_KEY).get("secretKey"),
            params.get(Input.APP_ID),
            params.get(Input.APP_KEY).get("secretKey"),
            self.logger,
        )

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

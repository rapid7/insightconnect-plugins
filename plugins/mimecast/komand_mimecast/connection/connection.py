import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from komand_mimecast.util.exceptions import ApiClientException
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

    def test_task(self):
        self.logger.info("Running a connection test to Mimecast")
        try:
            _, _, _ = self.client.get_siem_logs("")
            message = "The connection test to Mimecast was successful"
            self.logger.info(message)
            return {"success": True}, message
        except ApiClientException as error:

            return_message = ""

            failed_message = "The connection test to Mimecast has failed"
            self.logger.info(failed_message)
            return_message += f"{failed_message}\n"

            cause_message = f"This failure was caused by: {error.cause}"
            self.logger.info(cause_message)
            return_message += f"'{cause_message}'\n"

            self.logger.info(error.assistance)
            return_message += f"{error.assistance}\n"

            self.logger.error(error)
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=return_message)

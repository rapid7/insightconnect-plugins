import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from icon_automox.util.api_client import ApiClient
import time


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.automox_api = None
        self.api_key = None

    def connect(self, params):
        self.logger.info("Connect: Creating Client to Automox")
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.automox_api = ApiClient(self.logger, self.api_key)

    def test(self):
        start_time = time.time()

        try:
            self.automox_api.get_orgs()

            end_time = time.time()
            elapsed_time = int(end_time - start_time)

            self.automox_api.report_api_outcome(ApiClient.OUTCOME_SUCCESS, "connection_test", elapsed_time)
        except Exception as error:
            end_time = time.time()
            elapsed_time = int(end_time - start_time)
            failure_message = "Unable to list orgs during api test."

            self.automox_api.report_api_outcome(
                ApiClient.OUTCOME_FAIL, "connection_test", elapsed_time, failure_message
            )

            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error)

        return {}

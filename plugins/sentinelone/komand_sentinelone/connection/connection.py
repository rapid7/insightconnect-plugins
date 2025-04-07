import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import (
    ConnectionTestException,
    PluginException,
)
from komand_sentinelone.util.helper import format_subdomain
from komand_sentinelone.util.api import SentineloneAPI

ACTIVITIES_LOGS = "activities_logs"
EVENTS_LOGS = "events_logs"
THREATS_LOGS = "threats_logs"
API_VERSION = "2.1"


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        instance = format_subdomain(params.get(Input.INSTANCE, ""))
        self.client = SentineloneAPI(
            f"https://{instance}.sentinelone.net",
            params.get(Input.APIKEY, {}).get("secretKey"),
            self.logger,
        )

    def test(self):
        try:
            self.client.get_activity_types()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)

    def test_task(self):
        self.logger.info("Running a connection test to Sentinelone...")
        queries = [ACTIVITIES_LOGS, EVENTS_LOGS, THREATS_LOGS]
        total_queries = len(queries)
        total_failures = 0
        query_params = {"limit": 1}
        return_message = ""

        for query_type in queries:
            try:
                if query_type == ACTIVITIES_LOGS:
                    self.client.get_activities_list(query_params, True, True)
                elif query_type == EVENTS_LOGS:
                    self.client.get_device_control_events(query_params, True, True)
                else:
                    self.client.get_threats(query_params, API_VERSION, True, True)
                message = f"The connection test to Sentinelone for {query_type} was successful."
                self.logger.info(message)
                return_message += message + "\n"
            except PluginException as error:
                failed_message = f"The connection test to Sentinelone for {query_type} has failed."
                self.logger.info(failed_message)
                return_message += f"{failed_message}\n"

                cause_message = f"This failure was caused by: '{error.cause}'"
                self.logger.info(cause_message)
                return_message += f"{cause_message}\n"

                self.logger.info(error.assistance)
                return_message += f"{error.assistance}\n"

                total_failures += 1
                if total_failures >= total_queries:

                    failed_cause = "The connection test to Sentinelone has failed for each endpoint."
                    self.logger.info(failed_cause)
                    failed_assistance = "Please check your permissions and credentials before trying again."
                    self.logger.info(failed_assistance)

                    raise ConnectionTestException(
                        cause=failed_cause,
                        assistance=failed_assistance,
                        data=return_message,
                    )
        results_message = (
            f"The connection test was successful for {total_queries-total_failures}/{total_queries}" f" event types."
        )
        self.logger.info(results_message)
        return_message = f"{results_message}\n{return_message}"

        return {"success": True}, return_message

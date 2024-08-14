import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
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
        self.client = SentineloneAPI(
            f"https://{params.get(Input.INSTANCE)}.sentinelone.net",
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
        results = {ACTIVITIES_LOGS: {"success": True}, EVENTS_LOGS: {"success": True}, THREATS_LOGS: {"success": True}}

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
                message = f"The connection test to Sentinelone for {query_type} has failed."
                self.logger.info(message)
                return_message += message + "\n"

                error_data = {"cause": error.cause, "assistance": error.assistance, "data": error.data}
                results[query_type]["success"] = False
                results[query_type]["error"] = error_data

                total_failures += 1
                if total_failures >= total_queries:

                    failed_cause = "The connection test to Sentinelone has failed for each endpoint."
                    self.logger.info(failed_cause)
                    failed_assistance = "Please check your permissions and credentials before trying again."
                    self.logger.info(failed_assistance)
                    failed_data_message = f"Please see results of each query for more information: {results}"
                    self.logger.info(failed_data_message)

                    raise ConnectionTestException(cause=failed_cause, assistance=failed_assistance, data=results)
        results_message = (
            f"The connection test was successful for {total_queries-total_failures}/{total_queries}" f" event types."
        )
        self.logger.info(results_message)
        return_message = f"{results_message}\n{return_message}"
        if total_failures > 0:
            failures_message = f"The following failures were noted: {results}"
            self.logger.info(failures_message)
            return_message = f"{return_message}\n{failures_message}"
        return results, return_message

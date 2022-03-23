import insightconnect_plugin_runtime
from .schema import AdvancedQueryOnLogInput, AdvancedQueryOnLogOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import time
import json
from icon_rapid7_insightidr.util.parse_dates import parse_dates


class AdvancedQueryOnLog(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="advanced_query_on_log",
            description=Component.DESCRIPTION,
            input=AdvancedQueryOnLogInput(),
            output=AdvancedQueryOnLogOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        log_name = params.get(Input.LOG)
        timeout = params.get(Input.TIMEOUT)

        time_from_string = params.get(Input.TIME_FROM)
        relative_time_from = params.get(Input.RELATIVE_TIME)
        time_to_string = params.get(Input.TIME_TO)

        # Time To is optional, if not specified, time to is set to now
        time_from, time_to = parse_dates(time_from_string, time_to_string, relative_time_from)

        if time_from > time_to:
            raise PluginException(
                cause="Time To input was chronologically behind Time From.",
                assistance="Please edit the step so Time From is chronologically behind (in the past) relative to Time To.\n",
                data=f"\nTime From: {time_from}\nTime To:{time_to}",
            )

        log_id = self.get_log_id(log_name)

        # The IDR API will SOMETIMES return results immediately.
        # It will return results if it gets them. If not, we'll get a call back URL to work on
        callback_url, log_entries = self.maybe_get_log_entries(log_id, query, time_from, time_to)

        if not log_entries:
            log_entries = self.get_results_from_callback(callback_url, timeout)

        log_entries = insightconnect_plugin_runtime.helper.clean(log_entries)

        for log_entry in log_entries:
            log_entry["message"] = json.loads(log_entry.get("message", "{}"))

        self.logger.info(f"Sending results to orchestrator.")
        return {Output.RESULTS: log_entries, Output.COUNT: len(log_entries)}

    def get_results_from_callback(self, callback_url: str, timeout: int) -> [object]:
        """
        Get log entries from a callback URL

        @param callback_url: str
        @return: list of log entries
        """
        self.logger.info(f"Trying to get results from callback URL: {callback_url}")
        response = self.connection.session.get(callback_url)
        try:
            response.raise_for_status()
        except Exception:
            raise PluginException(
                cause="Failed to get logs from InsightIDR",
                assistance=f"Could not get logs from: {callback_url}",
                data=response.text,
            )
        results_object = response.json()
        log_entries = results_object.get("events")

        if results_object.get("links"):
            callback_url = results_object.get("links")[0].get("href")
        else:
            callback_url = ""

        counter = timeout
        while callback_url:
            counter -= 1
            if counter < 0:
                raise PluginException(
                    cause="Time out exceeded",
                    assistance="Time out for the query results was exceeded. Try simplifying your"
                    " query or extending the timeout period",
                )

            self.logger.info("Results were not ready. Sleeping 1 second and trying again.")
            self.logger.info(f"Time left: {counter}")
            self.logger.info(f"Progress: {results_object.get('progress')}")
            time.sleep(1)
            response = self.connection.session.get(callback_url)

            try:
                response.raise_for_status()
            except Exception:
                raise PluginException(
                    cause="Failed to get logs from InsightIDR\n",
                    assistance=f"Could not get logs from: {callback_url}\n",
                    data=response.text,
                )

            results_object = response.json()
            log_entries = results_object.get("events")
            if not log_entries:
                try:
                    callback_url = results_object.get("links")[0].get("href")
                except Exception:  # No results were found
                    self.logger.info("No results were found, returning an empty list")
                    return []
            else:
                return log_entries

        return log_entries

    def maybe_get_log_entries(self, log_id: str, query: str, time_from: int, time_to: int) -> (str, [object]):
        """
        Make a call to the API and ask politely for log results.

        If the query runs exceptionally fast the API will return results immediately. In this case, we will return the
        results as the second return entry in the return tuple. The first element of the tuple will be None

        Usually, the API will return a 202 with callback URL to poll for results. If this is the case, we
        return the URL as the first entry in the tuple return. The second element in the return tuple will be None

        @param log_id: str
        @param query: str
        @param time_from: int
        @param time_to: int
        @return: (callback url, list of log entries)
        """
        endpoint = f"{self.connection.url}log_search/query/logs/{log_id}"
        params = {"query": query, "from": time_from, "to": time_to}

        self.logger.info(f"Getting logs from: {endpoint}")
        self.logger.info(f"Using parameters: {params}")
        response = self.connection.session.get(endpoint, params=params)
        try:
            response.raise_for_status()
        except Exception:
            raise PluginException(
                cause="Failed to get logs from InsightIDR\n",
                assistance=f"Could not get logs from: {endpoint}\n",
                data=response.text,
            )

        results_object = response.json()
        potential_results = results_object.get("events")
        if potential_results:
            self.logger.info("Got results immediately, returning.")
            return None, potential_results
        else:
            self.logger.info("Got a callback url. Polling results...")
            return results_object.get("links")[0].get("href"), None

    def get_log_id(self, log_name: str) -> str:
        """
        Gets a log ID for a given log name

        @param log_name: str
        @return: str
        """
        endpoint = f"{self.connection.url}log_search/management/logs"

        self.logger.info(f"Getting log entries from: {endpoint}")
        response = self.connection.session.get(endpoint)
        try:
            response.raise_for_status()
        except Exception:
            raise PluginException(
                cause="Failed to get logs from InsightIDR",
                assistance=f"Could not get logs from: {endpoint}",
                data=response.text,
            )

        logs = response.json().get("logs")

        id = ""

        for log in logs:
            name = log.get("name")
            self.logger.info(f"Checking {log_name} against {name}")
            if name == log_name:
                self.logger.info("Log found.")
                id = log.get("id")
                break

        if id:
            self.logger.info(f"Found log with name {log_name} and ID: {id}")
            return id

        self.logger.error(f"Could not find log with name {log_name}")
        raise PluginException(
            cause="Could not find specified log.", assistance=f"Could not find log with name: {log_name}"
        )

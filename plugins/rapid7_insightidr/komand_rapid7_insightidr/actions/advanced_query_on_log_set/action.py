import insightconnect_plugin_runtime
from .schema import AdvancedQueryOnLogSetInput, AdvancedQueryOnLogSetOutput, Input, Output, Component

# Custom imports below
import time
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.util.parse_dates import parse_dates
from komand_rapid7_insightidr.util.util import send_session_request, get_logging_context
from requests import HTTPError
from uuid import uuid4
from typing import Tuple


class AdvancedQueryOnLogSet(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="advanced_query_on_log_set",
            description=Component.DESCRIPTION,
            input=AdvancedQueryOnLogSetInput(),
            output=AdvancedQueryOnLogSetOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        log_set_name = params.get(Input.LOG_SET)
        timeout = params.get(Input.TIMEOUT)

        time_from_string = params.get(Input.TIME_FROM)
        relative_time_from = params.get(Input.RELATIVE_TIME)
        time_to_string = params.get(Input.TIME_TO)

        statistical = self.parse_query_for_statistical(query)

        # Get request ID for logging context
        request_id = get_logging_context().get("R7-Correlation-Id", str(uuid4()))
        self.logger.info(f"Executing Advanced Query on Log Set action with Request ID: {request_id}")

        # Time To is optional, if not specified, time to is set to now
        time_from, time_to = parse_dates(time_from_string, time_to_string, relative_time_from)

        if time_from > time_to:
            raise PluginException(
                cause="Time To input was chronologically behind Time From.",
                assistance="Please edit the step so Time From is chronologically behind (in the past) relative to Time To.\n",
                data=f"\nTime From: {time_from}\nTime To:{time_to}",
            )

        log_set_id = self.get_log_set_id(log_set_name, request_id)

        # The IDR API will SOMETIMES return results immediately.
        # It will return results if it gets them. If not, we'll get a call back URL to work on
        callback_url, log_entries = self.maybe_get_log_entries(
            log_set_id, query, time_from, time_to, statistical, request_id
        )

        if callback_url and not log_entries:
            log_entries = self.get_results_from_callback(callback_url, timeout, statistical, request_id)
        if log_entries and not statistical:
            log_entries = ResourceHelper.get_log_entries_with_new_labels(
                self.connection, insightconnect_plugin_runtime.helper.clean(log_entries)
            )

        self.logger.info("Sending results to orchestrator.")

        if not statistical:
            return {Output.RESULTS_EVENTS: log_entries, Output.COUNT: len(log_entries)}
        else:
            return {
                Output.RESULTS_STATISTICAL: log_entries,
                Output.COUNT: log_entries.get("search_stats", {}).get("events_matched", 0),
            }

    @staticmethod
    def parse_query_for_statistical(query: str) -> bool:
        """
        Simple helper method to toggle the statistical boolean between true or false
        depending on whether the user's query contains a 'groupby()' or 'calculate()' clause.

        :param query: str
        :return: bool
        """

        for entry in ("calculate", "groupby"):
            if entry in query:
                return True

    def get_results_from_callback(
        self, callback_url: str, timeout: int, statistical: bool, request_id: str
    ) -> [object]:  # noqa: MC0001
        """
        Get log entries from a callback URL.

        :param callback_url: str - The URL to fetch logs from.
        :param timeout: int - How long to wait for results before timing out.
        :param statistical: bool - Whether to fetch statistical results or event logs.
        :param request_id: str - The request ID for logging context.
        :return: list of log entries or statistical data.
        """
        self.logger.info(f"Trying to get results from callback URL: {callback_url}")
        counter = timeout

        while callback_url and counter > 0:
            response = send_session_request(
                request_url=callback_url, request_headers=self.connection.headers, request_id=request_id
            )
            self.logger.info(f"IDR Response Status Code: {response.status_code}")

            try:
                # IDR seems to return both `raise_for_status` and `status_code` - value is in `status_code` / `raise_for_status` just returns `None`
                response.raise_for_status()
            except Exception as error:
                self.logger.error(f"Failed to get logs from InsightIDR: {error}")
                raise PluginException(
                    cause="Failed to get logs from InsightIDR",
                    assistance=f"Could not get logs from: {callback_url}",
                    data=response.text,
                )

            results_object = response.json()

            if "progress" in results_object:
                self.logger.info(f"Progress: {results_object.get('progress')}")
                while "progress" in results_object and counter > 0:
                    time.sleep(1)
                    counter -= 1
                    self.logger.info("Results were not ready. Sleeping 1 second and trying again.")
                    self.logger.info(f"Time left: {counter} seconds")
                    response = send_session_request(
                        request_url=callback_url, request_headers=self.connection.headers, request_id=request_id
                    )
                    try:
                        response.raise_for_status()
                        results_object = response.json()
                        if "progress" in results_object:
                            self.logger.info(f"Updated Progress: {results_object.get('progress')}")
                    except Exception as e:
                        self.logger.error(f"Failed to get logs during progress check: {e}")
                        raise PluginException(
                            cause="Failed to get logs during progress check",
                            assistance=f"Could not get logs from: {callback_url}",
                            data=response.text,
                        )

            if statistical:
                log_entries = results_object
            else:
                log_entries = results_object.get("events", [])

            # Check for the next link before deciding to return or continue
            # note: It seems even successful, completed results contain next link, so check for progress first
            next_link = next((link for link in results_object.get("links", []) if link.get("rel") == "Next"), None)

            if "progress" not in results_object:
                self.logger.info("No more results to process. Exiting.")
                return log_entries
            elif next_link:
                self.logger.info(
                    "Over 500 results are available for this query, but only a limited number will be returned. Please use a more specific query to get all results."
                )
                callback_url = next_link.get("href")

            counter -= 1
            if counter <= 0:
                self.logger.error("Timeout exceeded while waiting for logs.")
                raise PluginException(
                    cause="Time out exceeded",
                    assistance="Time out for the query results was exceeded. Try simplifying your query or extending the timeout period.",
                )

        self.logger.info("No valid log entries were fetched within the timeout period.")
        return {}

    def maybe_get_log_entries(
        self, log_id: str, query: str, time_from: int, time_to: int, statistical: bool, request_id: str
    ) -> Tuple[str, object]:
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
        @param statistical: bool
        @param request_id: str
        @return: (callback url, list of log entries)
        """
        endpoint = f"{self.connection.url}log_search/query/logsets/{log_id}"
        params = {"query": query, "from": time_from, "to": time_to}

        if not statistical:
            params["per_page"] = 500

        self.logger.info(f"Getting logs from: {endpoint}")
        self.logger.info(f"Using parameters: {params}")
        response = send_session_request(
            request_url=endpoint, request_params=params, request_headers=self.connection.headers, request_id=request_id
        )
        try:
            response.raise_for_status()
        except Exception:
            raise PluginException(
                cause="Failed to get log sets from InsightIDR\n",
                assistance=f"Could not get log sets from: {endpoint}\n",
                data=response.text,
            )

        results_object = response.json()

        if statistical:
            stats_endpoint = f"{self.connection.url}log_search/query/{results_object.get('id', '')}"
            self.logger.info(f"Getting statistical from: {stats_endpoint}")
            stats_response = send_session_request(
                request_url=stats_endpoint, request_headers=self.connection.headers, request_id=request_id
            )
            try:
                stats_response.raise_for_status()
            except HTTPError as error:
                raise PluginException(
                    cause="Failed to get log sets from InsightIDR\n",
                    assistance=f"Could not get statistical info from: {stats_endpoint}\n",
                    data=f"{stats_response.text}, {error}",
                )

            if stats_response.json().get("links"):
                potential_results = None
            else:
                potential_results = stats_response.json()
        else:
            potential_results = results_object.get("events")

        if potential_results:
            self.logger.info("Got results immediately, returning.")
            if results_object.get("links", [{}])[0].get("rel") == "Next":
                self.logger.info(
                    "Over 500 results are available for this query, but only 500 will be returned, please use a more specific query to get all results"
                )
            return None, potential_results
        else:
            self.logger.info("Got a callback url. Polling results...")
            return results_object.get("links", [{}])[0].get("href"), []

    def get_log_set_id(self, log_name: str, request_id: str) -> str:
        """
        Gets a log ID for a given log name

        @param log_name: str
        @param request_id: str
        @return: str
        """
        endpoint = f"{self.connection.url}log_search/management/logsets"

        self.logger.info(f"Getting log entries from: {endpoint}")
        response = send_session_request(
            request_url=endpoint, request_headers=self.connection.headers, request_id=request_id
        )
        try:
            response.raise_for_status()
        except Exception:
            raise PluginException(
                cause="Failed to get log sets from InsightIDR",
                assistance=f"Could not get log sets from: {endpoint}",
                data=response.text,
            )

        log_sets = response.json().get("logsets")

        log_id = ""

        for log_set in log_sets:
            name = log_set.get("name")
            self.logger.info(f"Checking {log_name} against {name}")
            if name == log_name:
                self.logger.info("Log set found.")
                log_id = log_set.get("id")
                break

        if log_id:
            self.logger.info(f"Found log set with name {log_name} and ID: {log_id}")
            return log_id

        self.logger.error(f"Could not find log set with name {log_name}")
        raise PluginException(
            cause="Could not find specified log set.", assistance=f"Could not find log set with name: {log_name}"
        )

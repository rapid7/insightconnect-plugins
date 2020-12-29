import komand
from .schema import AdvancedQueryInput, AdvancedQueryOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below
import time
from dateutil.parser import parse, ParserError


class AdvancedQuery(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='advanced_query',
                description=Component.DESCRIPTION,
                input=AdvancedQueryInput(),
                output=AdvancedQueryOutput())

    def run(self, params={}):
        query = params.get(Input.QUERY)
        log_name = params.get(Input.LOG)

        time_from_string = params.get(Input.TIME_FROM)
        time_to_string = params.get(Input.TIME_TO)

        time_from, time_to = self.parse_dates(time_from_string, time_to_string)

        log_id = self.get_log_id(log_name)

        # The IDR API will SOMETIMES return results immediately.
        # It will return results if it gets them. If not, we'll get a call back URL to work on
        callback_url, log_entries = self.maybe_get_log_entries(log_id, query, time_from, time_to)

        if not log_entries:
            log_entries = self.get_results_from_callback(callback_url)

        return {Output.RESULTS: log_entries}

    def parse_dates(self, time_from_string, time_to_string):
        # Parse times to epoch milliseconds
        try:
            time_from = int(parse(time_from_string).timestamp()) * 1000
            if time_to_string:
                time_to = int(parse(time_to_string).timestamp()) * 1000
            else:
                # Now in millisecond epoch time
                time_to = int(time.time()) * 1000
        except ParserError as e:
            raise PluginException(cause="Could not parse given date.",
                                  assistance="The date given was in an unrecognizable format.",
                                  data=e)
        return time_from, time_to

    def get_results_from_callback(self, callback_url):
        response = self.connection.session.get(callback_url)
        try:
            response.raise_for_status()
        except Exception:
            raise PluginException(cause="Failed to get logs from InsightIDR",
                                  assistance=f"Could not get logs from: {callback_url}",
                                  data=response.text)

        while not response.status_code == 200:
            time.sleep(1)
            response = self.connection.session.get(callback_url)

            # TODO: need to know what happens if we poll for a query that's not done
            try:
                response.raise_for_status()
            except Exception:
                raise PluginException(cause="Failed to get logs from InsightIDR",
                                      assistance=f"Could not get logs from: {callback_url}",
                                      data=response.text)

        results_object = response.json()
        return results_object.get("events")

    def maybe_get_log_entries(self, log_id, query, time_from, time_to):
        endpoint = f"{self.connection.url}log_search/query/logs/{log_id}"
        params = {
            "query": query,
            "from": time_from,
            "to": time_to
        }

        response = self.connection.session.get(endpoint, params=params)
        try:
            response.raise_for_status()
        except Exception:
            raise PluginException(cause="Failed to get logs from InsightIDR",
                                  assistance=f"Could not get logs from: {endpoint}",
                                  data=response.text)

        results_object = response.json()

        potential_results = results_object.get("events")
        if potential_results:
            return None, potential_results
        else:
            return results_object.get("links")[0].get("href"), None

    def get_log_id(self, log_name):
        endpoint = f"{self.connection.url}log_search/management/logs"
        response = self.connection.session.get(endpoint)

        try:
            response.raise_for_status()
        except Exception:
            raise PluginException(cause="Failed to get logs from InsightIDR",
                                  assistance=f"Could not get logs from: {endpoint}",
                                  data=response.text)

        logs = response.json().get("logs")

        id = ""
        for log in logs:
            name = log.get('name')
            self.logger.info(f"Checking {log_name} against {name}")
            if name == log_name:
                self.logger.info("Log found.")
                id = log.get("id")
                break

        if id:
            return id

        raise PluginException(cause="Could not find specified log.",
                              assistance=f"Could not find log with name: {log_name}")





import insightconnect_plugin_runtime
from .schema import (
    MonitorAlertsInput,
    MonitorAlertsOutput,
    MonitorAlertsState,
    Input,
    Output,
    Component,
    State,
)
import time
from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.exceptions import PluginException, APIException
from insightconnect_plugin_runtime.helper import response_handler, extract_json, hash_sha1, make_request
from typing import Any, Dict, Tuple
import requests
import urllib


TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
MAX_LOOKBACK_DAYS = 7
DEFAULT_LOOKBACK_HOURS = 24
# TODO - Changing alert limit had no effect
# Add default at end on var name
ALERT_LIMIT = 100
SORT_BY_FIELD = "last_modified_ts"

MAX_LIMIT = 7500

# State held values
LAST_ALERT_TIME = "last_alert_time"
LAST_ALERT_HASH = "last_alert_hash"
# State held values = CONOR
LAST_SEARCH_FROM = "last_search_from"
LAST_SEARCH_TO = "last_search_to"

# Used to paginate
ALERTS_OFFSET = "alerts_offset"
FROM_TIME_FILTER = "from_time_filter"
TO_TIME_FILTER = "to_time_filter"
TIMESTAMP_KEY = "event_timestamp"

NEXT_PAGE_LINK = "next_page_link"
# Custom imports below


class MonitorAlerts(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_alerts",
            description=Component.DESCRIPTION,
            input=MonitorAlertsInput(),
            output=MonitorAlertsOutput(),
            state=MonitorAlertsState(),
        )

    def run(self, params={}, state={}, custom_config: dict = {}):  # pylint: disable=unused-argument
        existing_state = state.copy()
        has_more_pages = False
        # TESTING PURPOSES
        custom_config = {
            "last_alert_time": {
                "date": {"year": 2024, "month": 8, "day": 1, "hour": 1, "minute": 2, "second": 3, "microsecond": 0}
            },
            "last_alert_time_days": 30,
            "max_last_alert_time": {
                "year": 2024,
                "month": 8,
                "day": 2,
                "hour": 3,
                "minute": 4,
                "second": 5,
                "microsecond": 0,
            },
            "alert_limit": 20,
        }

        try:

            now_time = self._get_current_time()
            start_time, alert_limit = self._parse_custom_config(custom_config, now_time, state)

            # TEMP TO RETRIEVE LOGS AS OLDEST ONE ISNT WITHIN LOOKBACK HOURS
            # start_time = 1694513478000

            self.logger.info("Starting to download alerts...")

            # todo - starttime needs to be last alert time or default lookback
            response, state, has_more_pages, status_code, error_message = self.get_alerts_palo_alto(
                state=state, start_time=start_time, end_time=now_time, alert_limit=alert_limit
            )

            # TODO - Are we supposed to show the total (MAX LIMIT) or the total (total_count)
            self.logger.info(f"Total alerts returned: {len(response)}")

            # Local Debugging
            self.logger.info(f"{type(response) = }")
            self.logger.info(f"{len(response) = }")
            self.logger.info(f"{state}, {has_more_pages = }")

            # TODO - Change first None to response
            # It's set to none so we can see all the logging without the results getting in the way
            # Note - when running locally, we should only get the first 100
            # When has more pages is True, the task will be rerun automatically again (on staging / the cloud exec)
            # If has more pages == True, then we need to change the search index from 0-100 to 101-200 (Done below now I think)

            return response, state, has_more_pages, status_code, error_message

        except PluginException as error:
            error_data = error.data.get("errors", [])

            if error_data:
                # if there is response data in the error then use it in the exception
                status_code = error_data[0].get("code")
                cause = error_data[0].get("message")

            else:
                status_code = 500
                cause = error.cause

            self.logger.error(
                f"A PluginException has occurred. Status code {status_code} returned. Error: {cause}. "
                f"Existing state: {existing_state}"
            )

            return [], existing_state, False, status_code, PluginException(cause=cause, data=error)

        except Exception as error:

            self.logger.error(
                f"An Unknown Exception has occurred. No results returned. Error: {error} "
                f"Existing state: {existing_state}"
            )

            return [], existing_state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    ###########################
    # Make request
    ###########################
    def get_alerts_palo_alto(self, state, start_time, end_time, alert_limit):
        endpoint = "public_api/v1/alerts/get_alerts"
        response_alerts_field = "alerts"
        time_sort_field = "creation_time"

        self.logger.info(f"{alert_limit = }")

        state.get(LAST_SEARCH_FROM)
        search_from = (state.get(LAST_SEARCH_TO) + 1) if state.get(LAST_SEARCH_FROM) else 0
        self.logger.info(f"{search_from = }")

        # IF NULL SET TO = 100
        state.get(LAST_SEARCH_TO)
        search_to = (search_from + 99) if state.get(LAST_SEARCH_TO) else 100

        state[LAST_SEARCH_FROM] = search_from
        state[LAST_SEARCH_TO] = search_to

        headers = self.connection.xdr_api.get_headers()

        filters = []
        filters = filters or []
        # If time constraints have been provided for the request, add them to the post body
        if start_time is not None and end_time is not None:
            filters.append({"field": time_sort_field, "operator": "gte", "value": start_time})
            filters.append({"field": time_sort_field, "operator": "lte", "value": end_time})

        post_body = {
            "request_data": {
                "search_from": search_from,
                "search_to": search_to,
                "sort": {"field": time_sort_field, "keyword": "desc"},
                "filters": filters,
            }
        }

        fqdn = self.connection.xdr_api.get_url()
        url = f"{fqdn}{endpoint}"

        # Local debugging
        self.logger.info(f"State in UpDate: {state = }")
        self.logger.info(f"{search_from = }")
        self.logger.info(f"{search_to = }")
        self.logger.info(f"{headers = }")
        self.logger.info(f"{post_body = }")
        self.logger.info(f"{url = }")

        request = requests.Request(method="post", url=url, headers=headers, json=post_body)
        response = make_request(request, timeout=120)

        response = extract_json(response)
        total_count = response.get("reply", {}).get("total_count", -1)
        result_count = response.get("reply", {}).get("result_count", -1)
        results = response.get("reply", {}).get(response_alerts_field, [])

        new_alerts, last_alert_hashes, last_alert_time = self._dedupe_and_get_highest_time(results, start_time, state)

        is_paginating = ALERT_LIMIT < total_count

        if is_paginating:
            has_more_pages = True
            state[LAST_SEARCH_FROM] = search_from
            state[LAST_SEARCH_TO] = search_to
            # state = {search_from: 0, search_to: 100}
            # next run it should then be
            # state = {search_from: 101, search_to: 200} or state = {search_from: 101, search_to: (total - search_from) (109 or whatever it equals)}
            # and so on

            self.logger.info(f"Found total alerts={total_count}, limit={ALERT_LIMIT}, is_paginating={is_paginating}")
            self.logger.info(
                f"Paginating alerts: Saving state with existing filters: "
                f"from_time={search_from}"
                f"to_time={search_to}"
            )

        else:
            has_more_pages = False
            state = self._drop_pagination_state(state)

        # add the last alert time to the state if it exists
        # if not then set to the last queried time to move the filter forward
        state[LAST_ALERT_TIME] = last_alert_time if last_alert_time else end_time
        # update hashes in state only if we've got new ones
        state[LAST_ALERT_HASH] = last_alert_hashes if last_alert_hashes else state.get(LAST_ALERT_HASH, [])

        return new_alerts, state, has_more_pages, 200, None

    ###########################
    # Deduping
    ###########################
    def _dedupe_and_get_highest_time(self, alerts: list, start_time: int, state: dict) -> Tuple[list, list, str]:
        """
        Function to dedupe alerts using existing hashes in the state, and return the highest
        timestamp.

        :param alerts: list of alerts
        :param state: state of the plugin
        :return: list of deduped alerts, list of new hashes, and the highest timestamp
        """

        old_hashes, deduped_alerts, new_hashes, highest_timestamp = state.get(LAST_ALERT_HASH, []), [], [], ""
        for index, alert in enumerate(alerts):
            alert_time = alert.get(TIMESTAMP_KEY)
            if alert_time == start_time:
                alert_hash = hash_sha1(alert)
                if alert_hash not in old_hashes:
                    deduped_alerts.append(alert)
            elif alert_time > start_time:
                deduped_alerts += alerts[index:]
                break

        num_alerts = len(deduped_alerts)
        self.logger.info(f"Received {len(alerts)} alerts, and after dedupe there is {num_alerts} results.")

        if deduped_alerts:
            # alert results are already sorted by CS API, so get the latest timestamp
            highest_timestamp = deduped_alerts[-1].get(TIMESTAMP_KEY)

            for alert in deduped_alerts:
                if alert.get(TIMESTAMP_KEY) == highest_timestamp:
                    new_hashes.append(hash_sha1(alert))
                    self.logger.info(f"Hashed latest event with timestamp {highest_timestamp}.")

            self.logger.debug(f"Highest timestamp is {highest_timestamp}")
            self.logger.debug(f"Last hash is {new_hashes}")

        return deduped_alerts, new_hashes, highest_timestamp

    @staticmethod
    def _get_current_time():
        # Gets the last 15 minutes in UNIX
        last_15_min = datetime.utcnow() - timedelta(minutes=15)
        return int(last_15_min.timestamp()) * 1000

    ###########################
    # Custom Config
    ###########################
    def _parse_custom_config(
        self, custom_config: Dict[str, Any], now: int, saved_state: Dict[int, str]
    ) -> Tuple[str, int]:
        """
        Takes custom config from CPS and allows the specification of a new start time for alerts,
        and allows the limit to be customised.

        :param custom_config: custom_config for the plugin
        :param now: datetime representing 'now'
        :param saved_state: existing state of the integration
        :return: string formatted time to apply to our alert queries, and limit integer to set how many
        alerts to fetch per run.
        """
        state = saved_state.copy()

        """
        As the DateTime object needs to contain milliseconds (as the log's UNIX time is in milliseconds),
        it does not come preset with milliseconds so this converts it to a string which allows for milliseconds
        to be added and after adding it gets converted back to a DateTime object, but with milliseconds added
        """
        dt_now = datetime.fromtimestamp(now / 1000, tz=timezone.utc)
        dt_now = dt_now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        dt_now = datetime.strptime(dt_now, "%Y-%m-%dT%H:%M:%S.%fZ")

        # set the alert limit from CPS if it exists, otherwise default to ALERT_LIMIT
        alert_limit = custom_config.get("alert_limit", ALERT_LIMIT)

        saved_time = state.get(LAST_ALERT_TIME)

        log_msg = ""
        if not saved_time:
            log_msg += "No previous alert time within state. "
            custom_timings = custom_config.get(LAST_ALERT_TIME, {})
            custom_date = custom_timings.get("date")
            custom_hours = custom_timings.get("hours", DEFAULT_LOOKBACK_HOURS)
            start = datetime(**custom_date) if custom_date else (dt_now - timedelta(hours=custom_hours))
            state[LAST_ALERT_TIME] = start.strftime(TIME_FORMAT)
        else:
            # check if we have held the TS beyond our max lookback
            lookback_days = custom_config.get(f"{LAST_ALERT_TIME}_days", MAX_LOOKBACK_DAYS)
            default_date_lookback = dt_now - timedelta(days=lookback_days)  # if not passed from CPS create on the fly
            custom_lookback = custom_config.get(f"max_{LAST_ALERT_TIME}", {})
            comparison_date = datetime(**custom_lookback) if custom_lookback else default_date_lookback
            comparison_date = comparison_date.replace(tzinfo=timezone.utc).strftime(TIME_FORMAT)
            if comparison_date > saved_time:
                self.logger.info(f"Saved time ({saved_time}) exceeds cut off, moving to ({comparison_date}).")
                state[LAST_ALERT_TIME] = comparison_date
                # pop state held time filters if they exist, incase customer has paused integration when paginating
                state = self._drop_pagination_state(state)

        start_time = state.get(LAST_ALERT_TIME)
        self.logger.info(f"{log_msg}Applying the following start time='{start_time}'. Limit={alert_limit}.")

        start_time = int(datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()) * 1000

        return start_time, alert_limit

    ###########################
    # Handle Pagination
    ###########################
    def _drop_pagination_state(self, state: Dict[str, str]) -> Dict[str, str]:
        """
        Helper function to pop values from the state if we need to break out of pagination.
        :return: state
        """
        log_msg = "Dropped the following keys from state: "
        if state.get(TO_TIME_FILTER):
            log_msg += f"{TO_TIME_FILTER}; "
            state.pop(TO_TIME_FILTER)

        if state.get(FROM_TIME_FILTER):
            log_msg += f"{FROM_TIME_FILTER}; "
            state.pop(FROM_TIME_FILTER)

        self.logger.debug(log_msg)

        return state

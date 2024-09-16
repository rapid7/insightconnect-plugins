import insightconnect_plugin_runtime
from requests import Response

from .schema import (
    MonitorAlertsInput,
    MonitorAlertsOutput,
    MonitorAlertsState,
    Component,
)
from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.exceptions import PluginException, ResponseExceptionData
from insightconnect_plugin_runtime.helper import extract_json, hash_sha1, make_request
from typing import Any, Dict, Tuple
import requests

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
MAX_LOOKBACK_DAYS = 7
DEFAULT_LOOKBACK_HOURS = 24
ALERT_LIMIT = 100

# State held values
LAST_ALERT_TIME = "last_alert_time"
LAST_ALERT_HASH = "last_alert_hash"

# Pagination
LAST_SEARCH_FROM = "last_search_from"
LAST_SEARCH_TO = "last_search_to"
TIMESTAMP_KEY = "event_timestamp"


class MonitorAlerts(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_alerts",
            description=Component.DESCRIPTION,
            input=MonitorAlertsInput(),
            output=MonitorAlertsOutput(),
            state=MonitorAlertsState(),
        )
        self.endpoint = "public_api/v1/alerts/get_alerts"
        self.response_alerts_field = "alerts"
        self.time_sort_field = "creation_time"

    def run(self, params={}, state={}, custom_config: dict = {}):  # pylint: disable=unused-argument
        existing_state = state.copy()
        # todo - TESTING PURPOSES
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

            self.logger.info("Starting to download alerts...")

            # todo - starttime needs to be last alert time or default lookback
            response, state, has_more_pages = self.get_alerts_palo_alto(
                state=state, start_time=start_time, end_time=now_time, alert_limit=alert_limit
            )

            return response, state, has_more_pages, 200, None

        except PluginException as error:
            if isinstance(error.data, Response):
                # if there is response data in the error then use it in the exception
                status_code = error.data.status_code
                cause = error.data.text
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
                f"Unknown exception has occurred. No results returned. Error: {error} "
                f"Existing state: {existing_state}"
            )
            return [], existing_state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    ###########################
    # Make request
    ###########################
    def get_alerts_palo_alto(self, state, start_time, end_time, alert_limit):

        self.logger.info(f"{alert_limit = }")

        search_from = (state.get(LAST_SEARCH_TO) + 1) if state.get(LAST_SEARCH_FROM) else 0
        self.logger.info(f"{search_from = }")

        # IF NULL SET TO = 100
        # todo - make changes on handling custom number of alerts
        search_to = (search_from + 99) if state.get(LAST_SEARCH_TO) else 100

        state[LAST_SEARCH_FROM] = search_from
        state[LAST_SEARCH_TO] = search_to

        filters = []
        # If time constraints have been provided for the request, add them to the post body
        if start_time is not None and end_time is not None:
            filters.append({"field": self.time_sort_field, "operator": "gte", "value": start_time})
            filters.append({"field": self.time_sort_field, "operator": "lte", "value": end_time})

        post_body = self.build_post_body(search_from=search_from, search_to=search_to, filters=filters)

        results, total_count = self.get_response(post_body=post_body)

        new_alerts, last_alert_hashes, last_alert_time = self._dedupe_and_get_highest_time(results, start_time, state)

        # todo - maybe alert_limit < result_count
        is_paginating = alert_limit < total_count

        has_more_pages = False

        if is_paginating:
            has_more_pages = True
            self.logger.info(f"Found total alerts={total_count}, limit={alert_limit}, is_paginating={is_paginating}")
            self.logger.info(
                f"Paginating alerts: Saving state with existing filters: "
                f"from_time={search_from}"
                f"to_time={search_to}"
            )

        # add the last alert time to the state if it exists
        # if not then set to the last queried time to move the filter forward
        state[LAST_ALERT_TIME] = last_alert_time if last_alert_time else end_time
        # update hashes in state only if we've got new ones
        state[LAST_ALERT_HASH] = last_alert_hashes if last_alert_hashes else state.get(LAST_ALERT_HASH, [])
        return new_alerts, state, has_more_pages

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
    ) -> Tuple[int, int]:
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

        dt_now = self.convert_unix_to_datetime(now)

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
                # state = self._drop_pagination_state(state)

        start_time = state.get(LAST_ALERT_TIME)
        self.logger.info(f"{log_msg}Applying the following start time='{start_time}'. Limit={alert_limit}.")

        # CONVERTS BACK TO EPOCH
        start_time = self.convert_to_unix(start_time)

        return start_time, alert_limit

    ###########################
    # Make request
    ###########################
    def get_response(self, post_body: dict):
        """
        Helper method to return the response JSON and total count
        """
        headers = self.connection.xdr_api.get_headers()

        fqdn = self.connection.xdr_api.get_url()
        url = f"{fqdn}{self.endpoint}"

        request = requests.Request(method="post", url=url, headers=headers, json=post_body)
        response = make_request(_request=request, timeout=60, exception_data_location=ResponseExceptionData.RESPONSE)

        response = extract_json(response)
        total_count = response.get("reply", {}).get("total_count", 0)
        results = response.get("reply", {}).get(self.response_alerts_field, [])

        return results, total_count

    ###########################
    # Build post body
    ###########################
    def build_post_body(self, search_from, search_to, filters):
        post_body = {
            "request_data": {
                "search_from": search_from,
                "search_to": search_to,
                "sort": {"field": self.time_sort_field, "keyword": "desc"},
                "filters": filters,
            }
        }
        return post_body

    def convert_unix_to_datetime(self, unix_time: int):
        return datetime.fromtimestamp(unix_time / 1000, tz=timezone.utc)

    def convert_to_unix(self, date_time):
        return int(datetime.strptime(date_time, TIME_FORMAT).timestamp()) * 1000

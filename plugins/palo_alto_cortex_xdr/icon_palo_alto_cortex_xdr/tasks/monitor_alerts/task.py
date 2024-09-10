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
ALERT_LIMIT = 100

MAX_LIMIT = 7500

# State held values
LAST_ALERT_TIME = "last_incident_time"
LAST_ALERT_HASH = "last_incident_hash"
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
        parameters = {}
        print(f"{existing_state = }")

        custom_config = {}
        state = {LAST_SEARCH_FROM: None, LAST_SEARCH_TO: None}

        try:

            now_time = self._get_current_time()
            now = now_time - timedelta(minutes=15)
            # last 15 minutes
            end_time = now.strftime(TIME_FORMAT)
            print(f"{end_time = }")
            start_time, alert_limit = self._parse_custom_config(custom_config, now, state)

            self.logger.info("Starting to download alerts...")

            response, state, has_more_pages = self.get_alerts_palo_alto(state=state, custom_config=custom_config)

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
            return response, state, has_more_pages, 200, None

        except PluginException as error:
            self.logger.error(
                f"A PluginException has occurred. Status code 500 returned. Error: {error.cause}. "
                f"Existing state: {existing_state}"
            )
            return [], existing_state, False, 500, PluginException(cause=error.cause, data=error)

        except Exception as error:
            print(f"{error = }")
            return [], existing_state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    ###########################
    # Make request
    ###########################
    def get_alerts_palo_alto(self, state, custom_config):
        endpoint = "/public_api/v1/alerts/get_alerts"
        response_alerts_field = "alerts"
        time_sort_field = "creation_time"

        self.logger.info(f"{ALERT_LIMIT = }")

        # IT GOES 0 -> 100 | 101 -> 200 | 201 -> 300
        # IF NULL, SET FROM = 0

        if not state.get(LAST_SEARCH_FROM):
            search_from = 0
        else:
            # STARTS 1 RECORD AFTER THE LAST ONE PULLED
            search_from = state.get(LAST_SEARCH_TO) + 1
            self.logger.info(f"{search_from = }")

        # IF NULL SET TO = 100
        if not state.get(LAST_SEARCH_TO):
            search_to = 100
        else:
            # SEARCH_TO GETS THE NEWEST SEARCH FROM VALUE AND WILL STOP AFTER PULLING 99 ADDITIONAL RECORDS (100 TOTAL)
            search_to = search_from + 99

        state[LAST_SEARCH_FROM] = search_from
        state[LAST_SEARCH_TO] = search_to

        # search_from = state.get(LAST_SEARCH_FROM, 0)
        # search_to = state.get(LAST_SEARCH_TO, 100) + 100
        # TODO - Figure out the hundreds i wanna cry

        # search_to = search_from + ALERT_LIMIT
        headers = self.connection.xdr_api.get_headers()

        post_body = {
            "request_data": {
                "search_from": search_from,
                "search_to": search_to,
                "sort": {"field": time_sort_field, "keyword": "asc"},
            }
        }

        url = urllib.parse.urljoin("https://api-rapid7.xdr.us.paloaltonetworks.com", endpoint)

        # Local debugging
        self.logger.info(f"State in UpDate: {state = }")
        self.logger.info(f"{search_from = }")
        self.logger.info(f"{search_to = }")
        self.logger.info(f"{headers = }")
        self.logger.info(f"{post_body = }")
        self.logger.info(f"{url = }")

        try:
            request = requests.Request(method="post", url=url, headers=headers, json=post_body)
            response = make_request(
                request, exception_custom_configs=custom_config, timeout=120, allowed_status_codes=[]
            )

            response = response.json()

            total_count = response.get("reply", {}).get("total_count", -1)
            result_count = response.get("reply", {}).get("result_count", -1)
            results = response.get("reply", {}).get(response_alerts_field, [])

            is_paginating = ALERT_LIMIT < total_count

            if is_paginating:
                has_more_pages = True
                state[LAST_SEARCH_FROM] = search_from
                state[LAST_SEARCH_TO] = search_to
                # state = {search_from: 0, search_to: 100}
                # next run it should then be
                # state = {search_from: 101, search_to: 200} or state = {search_from: 101, search_to: (total - search_from) (109 or whatever it equals)}
                # and so on

                self.logger.info(
                    f"Found total alerts={total_count}, limit={ALERT_LIMIT}, is_paginating={is_paginating}"
                )
                self.logger.info(
                    f"Paginating alerts: Saving state with existing filters: "
                    f"from_time={search_from}"
                    f"to_time={search_to}"
                )

            else:
                has_more_pages = False
                state = self._drop_pagination_state(state)

            return results, state, has_more_pages

        except PluginException as error:
            self.logger.error(
                f"A PluginException has occurred. Status code 500 returned. Error: {error.cause}. "
                f"Existing state: {state}"
            )
            return [], state, False, 500, PluginException(cause=error.cause, data=error)

        except Exception as error:
            print(f"{error = }")
            return [], state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    ###########################
    # Deduping
    ###########################
    def _dedupe_and_get_highest_time(self, alerts: list, start_time: str, state: dict) -> Tuple[list, list, str]:
        """
        Function to dedupe alerts using existing hashes in the state, and return the highest
        timestamp.

        :param alerts: list of alerts
        :param state: state of the plugin
        :return: list of deduped alerts, list of new hashes, and the highest timestamp
        """

        old_hashes, deduped_alerts, new_hashes, highest_timestamp = state.get(LAST_ALERT_HASH, []), [], [], ""
        for index, alert in enumerate(alerts):

            # todo - make method to convert
            alert_time = alert.get(TIMESTAMP_KEY) / 1000
            alert_time = datetime.fromtimestamp(alert_time, tz=timezone.utc).strftime(TIME_FORMAT)

            if alert_time == start_time:
                alert_hash = hash_sha1(alert)
                if alert_hash not in old_hashes:
                    deduped_alerts.append(alert)
            elif alert_time > start_time:
                deduped_alerts += alerts[index:]
                print(f"{deduped_alerts= }")
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
        return datetime.now(timezone.utc)

    ###########################
    # Custom Config
    ###########################
    def _parse_custom_config(
        self, custom_config: Dict[str, Any], now: datetime, saved_state: Dict[str, str]
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

        # set the alert limit from CPS if it exists, otherwise default to ALERT_LIMIT
        alert_limit = custom_config.get("alert_limit", ALERT_LIMIT)

        saved_time = state.get(LAST_ALERT_TIME)

        log_msg = ""
        if not saved_time:
            log_msg += "No previous alert time within state. "
            custom_timings = custom_config.get(LAST_ALERT_TIME, {})
            custom_date = custom_timings.get("date")
            custom_hours = custom_timings.get("hours", DEFAULT_LOOKBACK_HOURS)
            start = datetime(**custom_date) if custom_date else (now - timedelta(hours=custom_hours))
            state[LAST_ALERT_TIME] = start.strftime(TIME_FORMAT)
        else:
            # check if we have held the TS beyond our max lookback
            lookback_days = custom_config.get(f"{LAST_ALERT_TIME}_days", MAX_LOOKBACK_DAYS)
            default_date_lookback = now - timedelta(days=lookback_days)  # if not passed from CPS create on the fly
            custom_lookback = custom_config.get(f"max_{LAST_ALERT_TIME}", {})
            comparison_date = datetime(**custom_lookback) if custom_lookback else default_date_lookback
            comparison_date = comparison_date.replace(tzinfo=timezone.utc).strftime(TIME_FORMAT)
            if comparison_date > saved_time:
                self.logger.info(f"Saved time ({saved_time}) exceeds cut off, moving to ({comparison_date}).")
                state[LAST_ALERT_TIME] = comparison_date
                # pop state held time filters if they exist, incase customer has paused integration when paginating
                state = self._drop_pagination_state(state)

        start_time = state.get(LAST_ALERT_TIME)
        print(f"{start_time = }")
        if not state.get(FROM_TIME_FILTER):
            self.logger.info(f"{log_msg}Applying the following start time='{start_time}'. Limit={alert_limit}.")
        else:
            # we're paginating, this will be the value used to query for alerts
            self.logger.info(
                f"{log_msg}Applying the following start time='{state.get(FROM_TIME_FILTER)}'. " f"Limit={alert_limit}"
            )

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

    # def get_alerts(self, start_time: str, end_time: str, limit: int, state: dict) -> Tuple[list, bool, Dict[str, str]]:

    #     if limit > MAX_LIMIT:
    #         self.logger.info(
    #             f"Warning: The pagination limit has been reached." f"Moving to last incident time: [{start_time}]"
    #         )
    #         state = self._drop_pagination_state(state)

    #     start_time = state.get(FROM_TIME_FILTER, start_time)
    #     end_time = state.get(TO_TIME_FILTER, end_time)

    #     response = self.connection.xdr_api.get_alerts_two()

    #     alerts = response.get("all_items", [])
    #     total_count = response.get("total_count", 0)

    #     new_alerts = []
    #     last_alert_time, last_alert_hashes = "", []

    #     self.logger.info(f"Retrieved {total_count} alerts")

    #     # dedupe and get the highest timestamp
    #     new_alerts, last_alert_hashes, last_alert_time = self._dedupe_and_get_highest_time(alerts, start_time, state)

    #     is_paginating = limit < total_count

    #     self.logger.info(f"Found total alerts={total_count}, limit={limit}, is_paginating={is_paginating}")

    #     if is_paginating:
    #         has_more_pages = True

    #         state[FROM_TIME_FILTER] = start_time
    #         state[TO_TIME_FILTER] = end_time

    #         self.logger.info(
    #             f"Paginating alerts: Saving state with existing filters: "
    #             f"from_time={start_time}"
    #             f"to_time={end_time}"
    #         )
    #     else:
    #         has_more_pages = False

    #         state = self._drop_pagination_state(state)

    #     state[LAST_ALERT_TIME] = last_alert_time if last_alert_time else end_time
    #     state[LAST_ALERT_HASH] = last_alert_hashes if last_alert_hashes else state.get(LAST_ALERT_HASH, [])

    #     return new_alerts, has_more_pages, state

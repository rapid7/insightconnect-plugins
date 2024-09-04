import insightconnect_plugin_runtime
from .schema import (
    MonitorIncidentsInput,
    MonitorIncidentsOutput,
    MonitorIncidentsState,
    Input,
    Output,
    Component,
    State,
)

from datetime import datetime, timedelta, timezone
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Any, Dict, Tuple

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
MAX_LOOKBACK_DAYS = 7
DEFAULT_LOOKBACK_HOURS = 24
ALERT_LIMIT = 100

# todo - Could change to 7500
MAX_LIMIT = 10000

# State held values
LAST_ALERT_TIME = "last_incident_time"
LAST_ALERT_HASH = "last_incident_hash"
LAST_OBSERVATION_TIME = "last_observation_time"
LAST_OBSERVATION_HASHES = "last_observation_hashes"

# Used to paginate
ALERTS_OFFSET = "alerts_offset"
FROM_TIME_FILTER = "from_time_filter"
TO_TIME_FILTER = "to_time_filter"

NEXT_PAGE_LINK = "next_page_link"
# Custom imports below


class MonitorIncidents(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_incidents",
            description=Component.DESCRIPTION,
            input=MonitorIncidentsInput(),
            output=MonitorIncidentsOutput(),
            state=MonitorIncidentsState(),
        )

    def run(self, params={}, state={}, custom_config: dict = {}):  # pylint: disable=unused-argument
        existing_state = state.copy()
        has_more_pages = False
        parameters = {}
        print(f"{existing_state = }")

        # custom_config = {"alert_limit": 50}

        try:

            now_time = self._get_current_time()
            now = now_time - timedelta(minutes=15)
            # last 15 minutes
            end_time = now.strftime(TIME_FORMAT)
            print(f"{end_time = }")
            start_time, alert_limit = self._parse_custom_config(custom_config, now, state)

            self.logger.info("Starting to download alerts...")

            # on first run from_time = 24 hours ago, to_time = now()
            # On 2nd run, from_time = last saved state, to_time = now()
            logs_response = self.get_alerts(
                start_time=start_time, end_time=end_time, limit=alert_limit, state=existing_state
            )
            self.logger.info()

            return logs_response, state, has_more_pages, 200, None

            # output, has_more_pages, state = self.get_incidents(
            #     start_time=start_time, end_time=end_time, limit=alert_limit, state=state
            # )
        except Exception as error:
            print(f"{error = }")
            raise PluginException(cause="ruhroh", data=error)
        # except PluginException as error:
        #     self.logger.error(
        #         f"A PluginException has occurred. Status code {status_code} returned. Error: {error.cause}. "
        #         f"Existing state: {existing_state}"
        #     )

        # return [], existing_state, False, status_code, PluginException(cause=error.cause, data=error)

    def get_alerts(self, start_time: str, end_time: str, limit: int, state: dict) -> Tuple[list, bool, Dict[str, str]]:
        # override start_time with from_time filter in state if it exists (paginating)
        # TODO - offset

        start_time = state.get(FROM_TIME_FILTER, start_time)
        end_time = state.get(TO_TIME_FILTER, end_time)

        logs_response = self.connection.xdr_api.get_alerts_two(from_time=start_time, to_time=end_time)

        self.logger.info(f"Retrieved {len(logs_response)} alerts")
        if is_paginating:
            has_more_pages = True
        else:
            has_more_pages = False

        return logs_response, has_more_pages, state

    @staticmethod
    def _get_current_time():
        return datetime.now(timezone.utc)

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

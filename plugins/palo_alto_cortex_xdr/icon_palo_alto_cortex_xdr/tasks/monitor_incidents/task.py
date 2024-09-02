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
INCIDENT_LIMIT = 100

# State held values
LAST_INCIDENT_TIME = "last_incident_time"
LAST_INCIDENT_HASH = "last_incident_hash"
LAST_OBSERVATION_TIME = "last_observation_time"
LAST_OBSERVATION_HASHES = "last_observation_hashes"

# Used to paginate
ALERTS_OFFSET = "alerts_offset"
FROM_TIME_FILTER = "from_time_filter"
TO_TIME_FILTER = "to_time_filter"

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
        try:
            now_time = self._get_current_time()
            now = now_time - timedelta(minutes=15)  # last 15 minutes
            end_time = now.strftime(TIME_FORMAT)

            self.logger.info("Starting to download incidents...")

            output, has_more_pages, state = self.get_incidents(
                start_time=start_time, end_time=end_time, limit=alert_limit, state=state
            )

        except PluginException as error:
            self.logger.error(
                f"A PluginException has occurred. Status code {status_code} returned. Error: {error.cause}. "
                f"Existing state: {existing_state}"
            )

            return [], existing_state, False, status_code, PluginException(cause=error.cause, data=error)

    @staticmethod
    def _get_current_time():
        return datetime.now(timezone.utc)

    def _parse_custom_config(
        self, custom_config: Dict[str, Any], now: datetime, saved_state: Dict[str, str]
    ) -> Tuple[str, str, int, bool]:
        """
        Takes custom config from CPS and allows the specification of a new start time for either alerts or observations,
        and allows the page_size to be customised.

        :param custom_config: dictionary of values passed from CPS {"last_alert_time": {"date": {..}}..}
        :param now: current time to determine the start time for each CB type.
        :param saved_state: dictionary of state values held.
        :return: two string formatted times to apply to our alert and observation queries,
                 max page size integer, and a boolean indicating if we want to debug request times.
        """
        # take a copy of state so this logic will need to happen again if an exception occurs
        state = saved_state.copy()

        # set the page_size from CPS if it exists, otherwise default to PAGE_SIZE
        page_size = custom_config.get("page_size", INCIDENT_LIMIT)
        # this flag will be used to allow logging of request times for debugging
        debug = custom_config.get("debug", False)

        log_msg = ""
        for palo_type_time in LAST_INCIDENT_TIME:
            saved_time = state.get(palo_type_time)
            if not saved_time:
                log_msg += f"No {palo_type_time} within state. "
                custom_timings = custom_config.get(palo_type_time, {})
                custom_date = custom_timings.get("date")
                custom_minutes = custom_timings.get("minutes", DEFAULT_LOOKBACK)
                start = datetime(**custom_date) if custom_date else (now - timedelta(minutes=custom_minutes))
                state[palo_type_time] = start.strftime(TIME_FORMAT)
            else:
                # check if we have held the TS beyond our max lookback
                lookback_days = custom_config.get(f"{palo_type_time}_days", MAX_LOOKBACK)
                default_date_lookback = now - timedelta(days=lookback_days)  # if not passed from CPS create on the fly
                custom_lookback = custom_config.get(f"max_{palo_type_time}", {})
                comparison_date = datetime(**custom_lookback) if custom_lookback else default_date_lookback
                comparison_date = comparison_date.replace(tzinfo=timezone.utc).strftime(TIME_FORMAT)
                if comparison_date > saved_time:
                    self.logger.info(f"Saved time ({saved_time}) exceeds cut off, moving to ({comparison_date}).")
                    state[palo_type_time] = comparison_date

        alerts_start = state.get(LAST_INCIDENT_TIME)
        observation_start = state.get(LAST_OBSERVATION_TIME)

        self.logger.info(
            f"{log_msg}Applying the following start times: alerts='{alerts_start}' "
            f"and observations='{observation_start}'. Max pages: page_size='{page_size}'."
        )
        return alerts_start, observation_start, page_size, debug

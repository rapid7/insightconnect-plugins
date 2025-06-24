import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import monitor_task_delay
from .schema import MonitorAlertsInput, MonitorAlertsOutput, MonitorAlertsState, Component

# Custom imports below

from datetime import datetime, timedelta, timezone, tzinfo
from typing import Dict, Tuple, Any

from icon_carbon_black_cloud.util.helper_util import hash_sha1
from icon_carbon_black_cloud.util.exceptions import RateLimitException, HTTPErrorException
from icon_carbon_black_cloud.util.constants import (
    OBSERVATION_TYPES,
    OBSERVATION_TIME_FIELD,
    ALERT_TIME_FIELD,
    TIME_FORMAT,
)

# State values
RATE_LIMITED = "rate_limited_until"
LAST_ALERT_TIME = "last_alert_time"
LAST_ALERT_HASHES = "last_alert_hashes"
LAST_OBSERVATION_TIME = "last_observation_time"
LAST_OBSERVATION_HASHES = "last_observation_hashes"
LAST_OBSERVATION_JOB = "last_observation_job"
LAST_OBSERVATION_JOB_TIME = "last_observation_job_time"
OBSERVATION_QUERY_END_TIME = "observation_end_time"
OBSERVATION_JOB_OFFSET = "observation_job_offset"

# CB can return 10K per API and suggest that if more than this is returned to then query from last event time.
# This value can also be customised via CPS with the page_size property.
ALERT_PAGE_SIZE_DEFAULT = 200
OBSERVATION_PAGE_SIZE_DEFAULT = 7300
OBSERVATION_WINDOW = 3

DEFAULT_LOOKBACK = 5  # first look back time in minutes
MAX_LOOKBACK = 7  # allows saved state to be within 7 days to auto recover from an error
CUTOFF_HEADROOM_HOURS = 1


class MonitorAlerts(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_alerts",
            description=Component.DESCRIPTION,
            input=MonitorAlertsInput(),
            output=MonitorAlertsOutput(),
            state=MonitorAlertsState(),
        )

    @monitor_task_delay(timestamp_keys=[LAST_ALERT_TIME, LAST_OBSERVATION_TIME], default_delay_threshold="2d")
    def run(self, params={}, state={}, custom_config={}):  # pylint: disable=unused-argument # noqa: MC0001
        alerts_and_observations, has_more_pages, observations_has_more_pages, alerts_success = [], False, False, False

        try:
            rate_limited = state.get(RATE_LIMITED)
            now_time = self._get_current_time()
            if rate_limited:
                log_msg = f"Rate limit value stored in state: {rate_limited}. "
                if rate_limited > now_time.strftime(TIME_FORMAT):
                    log_msg += "Still within rate limiting period, skipping task execution..."
                    self.logger.info(log_msg)
                    return [], state, False, 200, None

                log_msg += "However no longer in rate limiting period, so task can be executed..."
                del state[RATE_LIMITED]
                self.logger.info(log_msg)

            # Force 'now' to be 15 minutes before now as CB Analytics alerts can be updated for up to 15 minutes
            # following the original backend_timestamp, after which time the alert is considered immutable.
            now = now_time - timedelta(minutes=15)

            # Check if we have made use of custom config to change the start times from DEFAULT_LOOKBACK
            (
                alerts_start,
                observations_start,
                alert_page_size,
                observation_page_size,
                observation_window,
                debug,
            ) = self._parse_custom_config(custom_config, now, state)

            # calculate end window
            calculated_end_window = datetime.strptime(observations_start, TIME_FORMAT).astimezone(
                timezone.utc
            ) + timedelta(hours=observation_window)
            alert_end_time = now.strftime(TIME_FORMAT)
            observability_end_time = (
                now.strftime(TIME_FORMAT)
                if now < calculated_end_window
                else calculated_end_window.strftime(TIME_FORMAT)
            )

            # Retrieve job ID from last run or trigger a new one
            observation_job_id = state.get(LAST_OBSERVATION_JOB)
            if not observation_job_id:
                self.logger.info("No observation job ID found in state, triggering a new job...")
                observation_job_id, state = self.trigger_observation_search_job(
                    observations_start, observability_end_time, observation_page_size, debug, state
                )

            alerts, alert_has_more_pages, state = self.get_alerts(
                alerts_start, alert_end_time, alert_page_size, debug, state
            )
            alerts_and_observations.extend(alerts)
            alerts_success = True

            if observation_job_id:
                observations, observations_has_more_pages, state = self.get_observations(
                    observation_job_id, observation_page_size, debug, state, now
                )
                alerts_and_observations.extend(observations)
            if observations_has_more_pages or alert_has_more_pages:
                has_more_pages = True
            self.logger.info(
                f"Returning a combined total of {len(alerts_and_observations)} alerts and observations, "
                f"with has_more_pages={has_more_pages}"
            )
            return alerts_and_observations, state, has_more_pages, 200, None
        except RateLimitException as rate_limit_error:
            self.logger.info(f"Rate limited on API, returning {(len(alerts_and_observations))} items...")
            state[RATE_LIMITED] = (self._get_current_time() + timedelta(minutes=5)).strftime(TIME_FORMAT)
            return alerts_and_observations, state, False, 200, rate_limit_error
        except HTTPErrorException as http_error:

            status_code, has_more_pages, error, state = self._handle_404_status_code(http_error, state, alerts_success)

            self.logger.info(
                "HTTP error from Carbon Black",
                error=http_error.cause,
                status_code=http_error.status_code,
                returning_code=status_code,
                state=state,
            )

            return alerts_and_observations, state, has_more_pages, status_code, error

        except Exception as error:
            self.logger.error(
                f"Hit an unexpected error during task execution. State={state}, Error={error}", exc_info=True
            )
            return alerts_and_observations, state, False, 500, error

    def get_alerts(
        self, start_alert_time: str, end_alert_time: str, page_size: int, debug: bool, state: Dict[str, str]
    ) -> Tuple[list, bool, Dict[str, str]]:
        alerts_has_more_pages = False
        endpoint = f"api/alerts/v7/orgs/{self.connection.org_key}/alerts/_search"
        url = f"{self.connection.base_url}/{endpoint}"

        payload = {
            "time_range": {"start": start_alert_time, "end": end_alert_time},
            "criteria": {},
            "start": "1",
            "rows": str(page_size),  # max number of results that can be returned
            "sort": [{"field": ALERT_TIME_FIELD, "order": "ASC"}],
        }
        self.logger.info(f"Querying alerts using parameters {payload['time_range']}")
        resp = self.connection.request_api(url, payload, debug=debug)

        alerts = resp.get("results", [])
        if alerts:
            # Check if we have not got all available alerts otherwise trigger task again to catch up quicker
            # Our query to CB can return page_size (custom or 2.5K) during one time frame,
            # but there could be more available.
            num_found = resp.get("num_found", 0)
            if num_found > page_size:
                self.logger.info(
                    f"Have not got all alerts for the searched time period. {num_found} found but "
                    f"query page size is set to {page_size}. Returning has more pages true..."
                )
                alerts_has_more_pages = True

            alerts, state = self._dedupe_and_get_last_time(alerts, state, start_alert_time, observations=False)
        else:
            self.logger.info("No alerts retrieved for time period searched...")
            state[LAST_ALERT_TIME] = end_alert_time
        self.logger.info(f"{LAST_ALERT_TIME} set to: {state[LAST_ALERT_TIME]}, has_more_pages={alerts_has_more_pages}")

        return alerts, alerts_has_more_pages, state

    def trigger_observation_search_job(
        self, start_time: str, end_time: str, page_size: int, debug: bool, state: Dict[str, str]
    ) -> Tuple[str, Dict]:
        endpoint = f"api/investigate/v2/orgs/{self.connection.org_key}/observations/search_jobs"
        index = state.get(OBSERVATION_JOB_OFFSET, 0)
        search_params = {
            "rows": page_size,
            "start": index,
            "fields": ["*"],
            "criteria": {"observation_type": OBSERVATION_TYPES},
            "sort": [{"field": OBSERVATION_TIME_FIELD, "order": "asc"}],
            "time_range": {"start": start_time, "end": end_time},
        }
        url = f"{self.connection.base_url}/{endpoint}"
        self.logger.info("Triggering observation search", time_start=start_time, time_end=end_time, start=index)
        observation_job_id = self.connection.request_api(url, search_params, debug=debug).get("job_id")

        state[OBSERVATION_QUERY_END_TIME] = end_time

        if observation_job_id:
            self.logger.info(
                f"Saving observation job ID {observation_job_id} to the state. "
                f"Will query this after polling for alerts..."
            )
            state[LAST_OBSERVATION_JOB] = observation_job_id
            # track when our jobs have been created to avoid them never finishing. Used in `_check_if_job_time_exceeded`
            state[LAST_OBSERVATION_JOB_TIME] = self._get_current_time().strftime(TIME_FORMAT)

            if not state.get(LAST_OBSERVATION_TIME):
                # First run of trying to get observations, save the start time for usage in `_dedupe_and_get_last_time`
                self.logger.info(f"No {LAST_OBSERVATION_TIME} in the state, saving checkpoint as {start_time}")
                state[LAST_OBSERVATION_TIME] = start_time

        return observation_job_id, state

    def get_observations(
        self, job_id: str, page_size: int, debug: bool, state: Dict[str, Any], now: datetime
    ) -> Tuple[list, bool, Dict[str, str]]:
        observations, has_more_pages = [], False
        endpoint = f"api/investigate/v2/orgs/{self.connection.org_key}/observations/search_jobs/{job_id}/results"

        # Strange CB API behaviour, unless rows param is specified it only returns 10 results
        url = f"{self.connection.base_url}/{endpoint}?rows={page_size}"
        self.logger.info(f"Get observation results from saved ID: {job_id}")
        observation_json = self.connection.request_api(url, request_method="GET", debug=debug)
        job_time_exceeded = self._check_if_job_time_exceeded(state.get(LAST_OBSERVATION_JOB_TIME), job_id)
        job_completed = observation_json.get("contacted") == observation_json.get("completed")
        if job_completed or job_time_exceeded:
            # only observations if the job is completed otherwise it is partial results and these are not sorted
            observations = observation_json.get("results", [])

            start_observation_time = state.get(LAST_OBSERVATION_TIME)
            if observations:
                # pass start time as the time saved in state - noticed 1 occasion CB API may return an observation
                # with a device_timestamp before queried window in which case we can't use this as the start time
                observations, state = self._dedupe_and_get_last_time(observations, state, start_observation_time)

                num_found = observation_json.get("num_found")
                if num_found > page_size:
                    self.logger.info(
                        f"More data is available on the API (num_found={num_found}) - setting has_more_pages=True..."
                    )
                    has_more_pages = True

            # we use if not observations, vs else, to ensure we pick up on the case where we dedupe every observation
            # it was noticed that during a Carbon Black API outage that if we did move the timestamp forward it was resulting in data gaps
            # in the event that job_time_exceeded is true but we haven't seen any observations we don't want to move the timestamp forward
            if not observations and not job_time_exceeded:
                state[LAST_OBSERVATION_TIME] = state.get(OBSERVATION_QUERY_END_TIME)

            if not has_more_pages:
                end_of_window = state.get(OBSERVATION_QUERY_END_TIME)
                has_more_pages = datetime.strptime(end_of_window, TIME_FORMAT).replace(tzinfo=timezone.utc) != now

            # remove the job ID as this is completed and next run we want to trigger a new one
            del state[LAST_OBSERVATION_JOB]
            del state[LAST_OBSERVATION_JOB_TIME]

            # if LAST_OBSERVATION_TIME hasn't got moved forward then we need to query the same time frame
            # this is because observations can arrive before the start time and also occur so frequently
            # that they can be returned in a page size but not move the time forward
            if state.get(LAST_OBSERVATION_TIME) <= start_observation_time:
                # if there is no observations found and the job time has been exceeded,
                # then we want to leave the offset at the same value to ensure there is no gaps
                if not observations and job_time_exceeded:
                    self.logger.info(
                        "Job time has been exceeded, but there was no observations found. Not increasing the page_size"
                    )
                    state[OBSERVATION_JOB_OFFSET] = state.get(OBSERVATION_JOB_OFFSET, 0)
                else:
                    state[OBSERVATION_JOB_OFFSET] = state.get(OBSERVATION_JOB_OFFSET, 0) + page_size
                state[LAST_OBSERVATION_TIME] = start_observation_time
                has_more_pages = True
            else:
                state.pop(OBSERVATION_JOB_OFFSET, None)

        else:
            self.logger.info("Job is not yet finished running, will get results in next task execution...")
            has_more_pages = True  # trigger again as it should be finished imminently (jobs run for a max of 3 minutes)

        self.logger.info(
            f"{LAST_OBSERVATION_TIME} set to: {state[LAST_OBSERVATION_TIME]}, has_more_pages={has_more_pages}"
        )
        return observations, has_more_pages, state

    def _dedupe_and_get_last_time(
        self, alerts: list, state: Dict[str, str], start_time: str, observations: bool = True
    ) -> Tuple[list, Dict]:
        last_hash_key, last_time_key, time_key = LAST_ALERT_HASHES, LAST_ALERT_TIME, ALERT_TIME_FIELD
        if observations:
            last_hash_key, last_time_key, time_key = (
                LAST_OBSERVATION_HASHES,
                LAST_OBSERVATION_TIME,
                OBSERVATION_TIME_FIELD,
            )

        old_hashes, deduped_alerts, new_hashes = state.get(last_hash_key, []), [], []
        # First dedupe and get the alerts we want to return nested list values may be re-ordered meaning a previously
        # returned alert or observation may change hash value. Safer to return than drop or manipulate source data.
        self.logger.info(f"Expecting to dedupe a max of {len(old_hashes)} based on previously stored hashes.")
        for index, alert in enumerate(alerts):
            alert_time = alert.get(time_key)
            # Observations quirk that it can return an alert time < start_time of the job search, should be in previous
            # run but return anyway as it won't be held in the hash values.
            if alert_time <= start_time and hash_sha1(alert) not in old_hashes:
                deduped_alerts.append(alert)
            elif alert_time > start_time:
                deduped_alerts += alerts[index:]  # we've gone past start time, keep the rest of the alerts
                break

        # Now grab the last time stamp and hash any alerts that match this as they could be returned in the next query
        num_alerts = len(deduped_alerts)
        self.logger.info(f"Received {len(alerts)}, and after dedupe there is {num_alerts} results.")
        if deduped_alerts:  # check we haven't deduped all results pulled back
            last_time = deduped_alerts[-1].get(time_key)
            for index in range(num_alerts - 1, -1, -1):
                alert = deduped_alerts[index]
                if alert.get(time_key) == last_time:
                    new_hashes.append(hash_sha1(deduped_alerts[index]))
                else:
                    break
            # update the state with these new values
            self.logger.info(f"Setting {last_time_key} to last parsed time: '{last_time}'")
            state[last_time_key], state[last_hash_key] = last_time, new_hashes
        return deduped_alerts, state

    def _parse_custom_config(
        self, custom_config: Dict[str, Any], now: datetime, saved_state: Dict[str, str]
    ) -> Tuple[str, str, int, int, int, bool]:
        """
        Takes custom config from CPS and allows the specification of a new start time for either alerts or observations,
        and allows the page_size to be customised.

        :param custom_config: dictionary of values passed from CPS {"last_alert_time": {"date": {..}}..}
        :param now: current time to determine the start time for each CB type.
        :param saved_state: dictionary of state values held.
        :return: two string formatted times to apply to our alert and observation queries,
                 alert_page_size integer, observation_page_size integer, and a boolean indicating if we want to debug request times.
        """
        # take a copy of state so this logic will need to happen again if an exception occurs
        state = saved_state.copy()

        # set the page_size from CPS if it exists, otherwise default to PAGE_SIZE
        alert_page_size = custom_config.get("alert_page_size", ALERT_PAGE_SIZE_DEFAULT)
        observation_page_size = custom_config.get("observation_page_size", OBSERVATION_PAGE_SIZE_DEFAULT)

        # window for observations
        observation_window = custom_config.get("observation_window", OBSERVATION_WINDOW)

        # this flag will be used to allow logging of request times for debugging
        debug = custom_config.get("debug", False)

        log_msg = ""
        for cb_type_time in [LAST_ALERT_TIME, LAST_OBSERVATION_TIME]:
            saved_time = state.get(cb_type_time)
            if not saved_time:
                log_msg += f"No {cb_type_time} within state. "
                custom_timings = custom_config.get(cb_type_time, {})
                custom_date = custom_timings.get("date")
                custom_minutes = custom_timings.get("minutes", DEFAULT_LOOKBACK)
                start = datetime(**custom_date) if custom_date else (now - timedelta(minutes=custom_minutes))
                state[cb_type_time] = start.strftime(TIME_FORMAT)
            else:
                # check if we have held the TS beyond our max lookback
                lookback_days = custom_config.get(f"{cb_type_time}_days", MAX_LOOKBACK)
                default_date_lookback = now - timedelta(days=lookback_days)  # if not passed from CPS create on the fly
                custom_lookback = custom_config.get(f"max_{cb_type_time}", {})
                comparison_date = datetime(**custom_lookback) if custom_lookback else default_date_lookback
                comparison_date_string = comparison_date.replace(tzinfo=timezone.utc).strftime(TIME_FORMAT)
                if comparison_date_string > saved_time:
                    headroom_date_string = (
                        (comparison_date + timedelta(hours=CUTOFF_HEADROOM_HOURS))
                        .replace(tzinfo=timezone.utc)
                        .strftime(TIME_FORMAT)
                    )
                    self.logger.info(
                        f"Saved time ({saved_time}) exceeds cut off of ({comparison_date_string}), moving to ({headroom_date_string})."
                    )
                    state[cb_type_time] = headroom_date_string
                    state.pop(OBSERVATION_JOB_OFFSET, None)

        alerts_start = state.get(LAST_ALERT_TIME)
        observation_start = state.get(LAST_OBSERVATION_TIME)

        self.logger.info(
            f"{log_msg}Applying the following start times: alerts='{alerts_start}' "
            f"and observations='{observation_start}'. Max pages: alert_page_size='{alert_page_size}, observation_page_size='{observation_page_size}'."
        )
        return alerts_start, observation_start, alert_page_size, observation_page_size, observation_window, debug

    def _check_if_job_time_exceeded(self, job_start_time: str, job_id: str) -> bool:
        """
        Jobs can only run within CB for a maximum of 3 minutes, allow a time frame of 4 minutes to complete otherwise we
        then we can assume that the job has been cancelled due to high usage on their platform and there will be
        a difference of 1 between the contacted and completed values and we should parse the available observations.
        """
        job_cut_off = (self._get_current_time() - timedelta(minutes=4)).strftime(TIME_FORMAT)

        if job_cut_off > job_start_time:
            self.logger.info(
                f"Job ({job_id}) has exceeded max run time. Started at {job_start_time}. Parsing available results..."
            )
            return True  # job time no longer valid - parse available results

        return False  # job time is still valid - honor contact vs completed values

    def _handle_404_status_code(
        self, http_exception: HTTPErrorException, state: Dict[str, str], alerts_success: bool
    ) -> tuple[int, bool, HTTPErrorException, Dict[str, str]]:
        """
        In the case that the observation ID from CB is no longer available and we return a 404, we should delete this ID
        from the state so that the next run can move on and not continually poll for this missing job.
        """

        has_more_pages = False
        status_code = http_exception.status_code
        http_error = http_exception
        if alerts_success and status_code == 404:
            observation_job_id = state.get(LAST_OBSERVATION_JOB)
            if observation_job_id:
                self.logger.error(
                    f"Received a 404 when trying to retrieve the job - '{observation_job_id}'. "
                    "Removing this job from the state to continue on the next run..."
                )
                # Only delete the observation ID and the time this was triggered
                # But keep the hashes and timings in the state for the next job
                status_code = 200
                has_more_pages = True
                http_error = None
                del state[LAST_OBSERVATION_JOB]
                del state[LAST_OBSERVATION_JOB_TIME]

        return status_code, has_more_pages, http_error, state

    @staticmethod
    def _get_current_time():
        return datetime.now(timezone.utc)
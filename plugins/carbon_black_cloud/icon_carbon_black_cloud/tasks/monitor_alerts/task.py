import insightconnect_plugin_runtime
from .schema import MonitorAlertsInput, MonitorAlertsOutput, MonitorAlertsState, Component

# Custom imports below

from datetime import datetime, timedelta, timezone
from typing import Dict, Tuple, Any

from icon_carbon_black_cloud.util.helper_util import hash_sha1
from icon_carbon_black_cloud.util.exceptions import RateLimitException, HTTPErrorException
from icon_carbon_black_cloud.util.constants import OBSERVATION_TYPES

ALERT_TIME_FIELD = "backend_timestamp"
OBSERVATION_TIME_FIELD = "device_timestamp"
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

# State held values
RATE_LIMITED = "rate_limited_until"
LAST_ALERT_TIME = "last_alert_time"
LAST_ALERT_HASHES = "last_alert_hashes"
LAST_OBSERVATION_TIME = "last_observation_time"
LAST_OBSERVATION_HASHES = "last_observation_hashes"
LAST_OBSERVATION_JOB = "last_observation_job"
LAST_OBSERVATION_JOB_TIME = "last_observation_job_time"

# CB can return 10K per API and suggest that if more than this is returned to then query from last event time.
# To prevent overloading IDR/PIF drop this limit to 2.5k on each endpoint.
# This value can also be customised via CPS with the page_size property.
PAGE_SIZE = 2500

DEFAULT_LOOKBACK = 5  # first look back time in minutes
MAX_LOOKBACK = 7  # allows saved state to be within 7 days to auto recover from an error


class MonitorAlerts(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_alerts",
            description=Component.DESCRIPTION,
            input=MonitorAlertsInput(),
            output=MonitorAlertsOutput(),
            state=MonitorAlertsState(),
        )

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
            end_time = now.strftime(TIME_FORMAT)

            # Check if we have made use of custom config to change the start times from DEFAULT_LOOKBACK
            alerts_start, observations_start, page_size, debug = self._parse_custom_config(custom_config, now, state)

            # Retrieve job ID from last run or trigger a new one
            observation_job_id = state.get(LAST_OBSERVATION_JOB)
            if not observation_job_id:
                self.logger.info("No observation job ID found in state, triggering a new job...")
                observation_job_id, state = self.trigger_observation_search_job(
                    observations_start, end_time, page_size, debug, state
                )

            alerts, alert_has_more_pages, state = self.get_alerts(alerts_start, end_time, page_size, debug, state)
            alerts_and_observations.extend(alerts)
            alerts_success = True

            if observation_job_id:
                observations, observations_has_more_pages, state = self.get_observations(
                    observation_job_id, page_size, debug, state
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
            state = self._update_state_in_404(http_error.status_code, state, alerts_success)
            self.logger.info(
                f"HTTP error from Carbon Black. State={state}, Status code={http_error.status_code}, returning"
                f" {(len(alerts_and_observations))} items..."
            )
            return alerts_and_observations, state, False, http_error.status_code, http_error
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
        search_params = {
            "rows": page_size,
            "start": 0,
            "fields": ["*"],
            "criteria": {"observation_type": OBSERVATION_TYPES},
            "sort": [{"field": OBSERVATION_TIME_FIELD, "order": "asc"}],
            "time_range": {"start": start_time, "end": end_time},
        }
        url = f"{self.connection.base_url}/{endpoint}"
        self.logger.info(f"Triggering observation search using parameters {search_params['time_range']}")
        observation_job_id = self.connection.request_api(url, search_params, debug=debug).get("job_id")

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
        self, job_id: str, page_size: int, debug: bool, state: Dict[str, str]
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
            if observations:
                # pass start time as the time saved in state - noticed 1 occasion CB API may return an observation
                # with a device_timestamp before queried window in which case we can't use this as the start time
                start_observation_time = state.get(LAST_OBSERVATION_TIME)
                observations, state = self._dedupe_and_get_last_time(observations, state, start_observation_time)

                if observation_json.get("num_found") > page_size:
                    self.logger.info("More data is available on the API - setting has_more_pages=True...")
                    has_more_pages = True
            # remove the job ID as this is completed and next run we want to trigger a new one
            del state[LAST_OBSERVATION_JOB]
            del state[LAST_OBSERVATION_JOB_TIME]
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
            if (alert_time == start_time and hash_sha1(alert) not in old_hashes) or alert_time < start_time:
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
        page_size = custom_config.get("page_size", PAGE_SIZE)
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
                comparison_date = comparison_date.replace(tzinfo=timezone.utc).strftime(TIME_FORMAT)
                if comparison_date > saved_time:
                    self.logger.info(f"Saved time ({saved_time}) exceeds cut off, moving to ({comparison_date}).")
                    state[cb_type_time] = comparison_date

        alerts_start = state.get(LAST_ALERT_TIME)
        observation_start = state.get(LAST_OBSERVATION_TIME)

        self.logger.info(
            f"{log_msg}Applying the following start times: alerts='{alerts_start}' "
            f"and observations='{observation_start}'. Max pages: page_size='{page_size}'."
        )
        return alerts_start, observation_start, page_size, debug

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

    def _update_state_in_404(self, status_code: int, state: Dict[str, str], alerts_success: bool) -> Dict[str, str]:
        """
        In the case that the observation ID from CB is no longer available and we return a 404, we should delete this ID
        from the state so that the next run can move on and not continually poll for this missing job.
        """
        if alerts_success and status_code == 404:
            observation_job_id = state.get(LAST_OBSERVATION_JOB)
            if observation_job_id:
                self.logger.error(
                    f"Received a 404 when trying to retrieve the job - '{observation_job_id}'. "
                    "Removing this job from the state to continue on the next run..."
                )
                # Only delete the observation ID and the time this was triggered
                # But keep the hashes and timings in the state for the next job
                del state[LAST_OBSERVATION_JOB]
                del state[LAST_OBSERVATION_JOB_TIME]
        return state

    @staticmethod
    def _get_current_time():
        return datetime.now(timezone.utc)

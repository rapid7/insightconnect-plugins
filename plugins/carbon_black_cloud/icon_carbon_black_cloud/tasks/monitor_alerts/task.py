import insightconnect_plugin_runtime
from .schema import MonitorAlertsInput, MonitorAlertsOutput, MonitorAlertsState, Component
# Custom imports below

from datetime import datetime, timedelta, timezone

from ...util.helper_util import hash_sha1
from ...util.constants import OBSERVATION_TYPES

ALERT_TIME_FIELD = "backend_timestamp"
OBSERVATION_TIME_FIELD = "device_timestamp"
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

LAST_ALERT_TIME = "last_alert_time"
LAST_ALERT_HASHES = "last_alert_hashes"
LAST_ALERT_PAGE = 0
LAST_OBSERVATION_TIME = "last_observation_time"
LAST_OBSERVATION_HASHES= "last_observation_hashes"
LAST_OBSERVATION_JOB = "last_observation_job"

# CB can return 10K per API and suggest  if more than this is returned to then query from last event time.
# To prevent overloading IDR/PIF drop this limit to 2.5k on each endpoint.
PAGE_SIZE = 2500


class MonitorAlerts(insightconnect_plugin_runtime.Task):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="monitor_alerts",
                description=Component.DESCRIPTION,
                input=MonitorAlertsInput(),
                output=MonitorAlertsOutput(),
                state=MonitorAlertsState())

    def run(self, params={}, state={}, custom_config={}):
        try:
            # TODO: add custom_config logic
            # Force now to be 15 minutes from 'now' as CB Analytics alerts can be updated for up to 15 minutes following
            # the original backend_timestamp, after which time the alert is considered immutable.
            now = datetime.now(timezone.utc) - timedelta(minutes=15)
            end_time = now.strftime(TIME_FORMAT)
            alerts_and_observations, has_more_pages, observations_has_more_pages = [], False, False

            # TODO: do we have any backoff times in the state for any endpoint
            alerts_start = state.get(LAST_ALERT_TIME)
            observations_start = state.get(LAST_OBSERVATION_TIME, (now - timedelta(minutes=5)).strftime(TIME_FORMAT))
            # Retrieve job ID from last run or trigger a new one
            observation_job_id = state.get(LAST_OBSERVATION_JOB)
            if not observation_job_id:
                self.logger.info("No observation job ID found in state, triggering a new job...")
                observation_job_id = self.trigger_observation_search_job(observations_start, end_time)
                if observation_job_id:
                    self.logger.info(f"Saving observation job ID {observation_job_id} to the state...")
                    state[LAST_OBSERVATION_JOB] = observation_job_id

                if not state.get(LAST_OBSERVATION_TIME):
                    # We should only hit this when we have *never* returned any observations.
                    self.logger.info(f"No {LAST_OBSERVATION_TIME} in the state, saving checkpoint as {observations_start}")

            if not alerts_start:
                self.logger.info("First run retrieving alerts...")
                alerts_start = (now - timedelta(minutes=5)).strftime(TIME_FORMAT)

            alerts, alert_has_more_pages, state = self.get_alerts(alerts_start, end_time, state)
            alerts_and_observations.extend(alerts)

            if observation_job_id:
                observations, observations_has_more_pages, state = self.get_observations(observation_job_id, state)
                alerts_and_observations.extend(observations)
            if observations_has_more_pages or alert_has_more_pages:
                has_more_pages = True
            self.logger.info(f"Returning a combined total of {len(alerts_and_observations)} alerts and observations, "
                             f"with has_more_pages={has_more_pages}")
            return alerts_and_observations, state, has_more_pages, 200, None
        except Exception as error:
            self.logger.error(f"Hit an unexpected error during task execution. Error={error}", exc_info=True)
            return [], state, False, 500, error

    def get_alerts(self, start_alert_time: str, end_alert_time: str, state):
        alerts_has_more_pages = False
        endpoint = f"api/alerts/v7/orgs/{self.connection.org_key}/alerts/_search"
        url = f"{self.connection.base_url}/{endpoint}"

        payload = {
            "time_range": {
                "start": start_alert_time,
                "end": end_alert_time
            },
            "criteria": {},
            "start": "1",
            "rows": str(PAGE_SIZE),  # max number of results that can be returned
            "sort": [{"field": ALERT_TIME_FIELD, "order": "ASC"}]
        }
        self.logger.info(f"Querying alerts using parameters {payload['time_range']}")
        resp = self.connection.post_to_api(url, payload)

        no_alerts, alerts = 0, resp.get("results", [])
        if alerts:
            # Check if we have not got all available alerts otherwise trigger task again to catch up quicker
            # CB can return max 10K during on time frame in which case we need to shorten the frame
            if resp.get("num_found", 0) > PAGE_SIZE:
                self.logger.info("Have not got all alerts for given time period. Returning has more pages true...")
                alerts_has_more_pages = True

            alerts, state = self._dedupe_and_get_last_time(alerts, state, start_alert_time, observations=False)
        else:
            self.logger.info("No alerts retrieved for time period searched...")
            state[LAST_ALERT_TIME] = end_alert_time
        self.logger.info(f"Next time set to: {state[LAST_ALERT_TIME]}, has_more_pages={alerts_has_more_pages}")

        return alerts, alerts_has_more_pages, state

    def trigger_observation_search_job(self, start_time: str, end_time: str):
        endpoint = f"api/investigate/v2/orgs/{self.connection.org_key}/observations/search_jobs"
        search_params = {
            "rows": PAGE_SIZE,
            "start": 0,
            "fields": ["*"],
            "criteria": {"observation_type": OBSERVATION_TYPES},
            "sort": [{"field": "device_timestamp","order": "asc"}],
            "time_range": {"end": end_time, "start": start_time}
        }
        url = f"{self.connection.base_url}/{endpoint}"
        self.logger.info(f"Triggering observation search using parameters {search_params['time_range']}")
        observation_resp = self.connection.post_to_api(url, search_params)

        return observation_resp.get("job_id")

    def get_observations(self, job_id: str, state: dict):
        observations, has_more_pages = [], False
        endpoint = f"api/investigate/v2/orgs/{self.connection.org_key}/observations/search_jobs/{job_id}/results"

        # Strange CB API behaviour, unless rows param is specified it only returns 10 results
        url = f"{self.connection.base_url}/{endpoint}?rows={PAGE_SIZE}"
        self.logger.info(f"Get observation results from saved ID: {job_id}")
        observation_resp = self.connection.get_from_api(url)
        observation_json = observation_resp.json()
        if observation_json.get("contacted") != observation_json.get("completed"):
            self.logger.info("Job is not yet finished running, will get results in next task execution...")
            has_more_pages = True  # trigger again as it should be finished imminently (jobs run for a max of 3 minutes)
        else:
            # only observations if the job is completed otherwise it is partial results and these are not sorted
            observations = observation_json.get("results")
            if observations:
                start_observation_time = observations[0].get(OBSERVATION_TIME_FIELD)
                observations, state = self._dedupe_and_get_last_time(observations, state, start_observation_time)

                if observation_json.get('num_found') > PAGE_SIZE:
                    self.logger.info("more data is available on the API - setting has more pages to true...")
                    has_more_pages = True
            # remove the job ID as this is completed and next run we want to trigger a new one
            del state[LAST_OBSERVATION_JOB]

        return observations, has_more_pages, state

    def _dedupe_and_get_last_time(self, alerts, state, start_time, observations=True):
        last_hash_key, last_time_key, time_key = LAST_ALERT_HASHES, LAST_ALERT_TIME, ALERT_TIME_FIELD
        if observations:
            last_hash_key, last_time_key, time_key = LAST_OBSERVATION_HASHES, LAST_OBSERVATION_TIME, OBSERVATION_TIME_FIELD

        old_hashes, deduped_alerts, new_hashes = state.get(last_hash_key, []), [], []
        # First dedupe and get the alerts we want to return
        self.logger.info(f"Expecting to dedupe {len(old_hashes)} based on previously stored hashes.")
        for index, alert in enumerate(alerts):
            alert_time = alert.get(time_key)
            if alert_time == start_time and hash_sha1(alert) not in old_hashes:
                deduped_alerts.append(alert)
            elif alert_time > start_time:
                deduped_alerts += alerts[index:]  # we've gone past start time, keep the rest of the alerts
                break

        # Now grab the last time stamp and hash any alerts that match this as they could be returned in the next query
        no_alerts = len(deduped_alerts)
        self.logger.info(f"Received {len(alerts)}, and after dedupe there is {no_alerts} results.")
        last_time = deduped_alerts[-1].get(time_key)
        for index in range(no_alerts-1, -1, -1):
            alert = deduped_alerts[index]
            if alert.get(time_key) == last_time:
                new_hashes.append(hash_sha1(deduped_alerts[index]))
            else:
                break

        # update the state with these new values
        state[last_time_key], state[last_hash_key] = last_time, new_hashes
        return deduped_alerts, state

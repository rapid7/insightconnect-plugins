import time

import insightconnect_plugin_runtime

# Custom imports below
import json
from datetime import datetime, timedelta, timezone

from icon_azure_sentinel.util.tools import generate_query_params
from .schema import Component, GetNewIncidentsInput, GetNewIncidentsOutput, Input, Output
from pathlib import Path
from tempfile import gettempdir

CACHE_FILE = "get_new_incidents_cache.json"
LAST_EXECUTION_KEY = "last_execution"
SLIDING_WINDOW_DELAY = 5  # seconds
FIRST_RUN_LOOKBACK_TIME = 12 * 60  # 12 hours in minutes


class GetNewIncidents(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_new_incidents",
            description=Component.DESCRIPTION,
            input=GetNewIncidentsInput(),
            output=GetNewIncidentsOutput(),
        )
        self.cache_path = Path(gettempdir()) / CACHE_FILE  # nosec

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        subscription_id = params.get(Input.SUBSCRIPTIONID, "")
        resource_group_name = params.get(Input.RESOURCEGROUPNAME, "")
        workspace_name = params.get(Input.WORKSPACENAME, "")
        interval = abs(params.get(Input.INTERVAL))
        status = params.get(Input.STATUS, "")
        last_update_time = (
            datetime.fromisoformat(params.get(Input.LAST_UPDATE_TIME, "")).replace(tzinfo=None)
            if params.get(Input.LAST_UPDATE_TIME, "")
            else None
        )
        assigned_to = params.get(Input.ASSIGNED_TO, "")
        first_run_lookback_time = (
            abs(params.get(Input.FIRST_RUN_LOOKBACK_TIME, FIRST_RUN_LOOKBACK_TIME)) or FIRST_RUN_LOOKBACK_TIME
        )
        # END INPUT BINDING - DO NOT REMOVE

        # Initial lookback time for requests
        last_execution_time = self._calculate_next_execution(first_run_lookback_time=first_run_lookback_time)
        while True:
            # Generate filter parameters for request
            self.logger.info(f"Checking for new incidents from {last_execution_time.isoformat()}")
            filters = generate_query_params(status, last_execution_time, last_update_time, assigned_to)

            # Fetch new incidents
            incidents, _ = self.connection.api_client.list_incident(
                resource_group_name, workspace_name, filters, subscription_id
            )

            # If incidents were found, return
            if incidents:
                self.logger.info(f"Found {len(incidents)} new incident(s). Sending to orchestrator.")
                self.send({Output.INCIDENTS: incidents})
            else:
                self.logger.info("No new incidents have been found.")

            # Persist cursor after successful poll and advance for next cycle
            self._save_last_execution(self._get_now_delayed())
            self.logger.info(f"Saved last execution time to cache: {last_execution_time.isoformat()}")
            last_execution_time = self._calculate_next_execution(
                first_run_lookback_time=first_run_lookback_time, fallback=last_execution_time
            )

            self.logger.info(f"Sleeping for {interval} seconds...")
            time.sleep(interval)

    def _load_last_execution(self):
        try:
            if self.cache_path.exists():
                with self.cache_path.open("r") as file_:
                    if last_execution := json.loads(file_.read()).get(LAST_EXECUTION_KEY):
                        return datetime.fromisoformat(last_execution)
        except Exception as error:
            self.logger.error(f"Failed to load cache: {error}")

    def _save_last_execution(self, execution_time: datetime) -> None:
        try:
            with self.cache_path.open("w") as file_:
                json.dump({LAST_EXECUTION_KEY: execution_time.isoformat()}, file_)
        except Exception as error:
            self.logger.error(f"Failed to save cache: {error}")

    @staticmethod
    def _get_now_delayed() -> datetime:
        return datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(seconds=SLIDING_WINDOW_DELAY)

    def _calculate_next_execution(self, first_run_lookback_time: int, fallback: datetime | None = None) -> datetime:
        # If there's a cached last execution, resume from there
        if last_execution := self._load_last_execution():
            self.logger.info(f"Resuming from cached last execution: {last_execution.isoformat()}")
            return last_execution

        # If cache is unavailable but we have an in-memory fallback, use it
        if fallback is not None:
            self.logger.info(f"Cache unavailable, using in-memory fallback: {fallback.isoformat()}")
            return fallback

        # No cache and no fallback — first run, apply lookback window
        self.logger.info(
            f"First run detected. Initialising trigger with lookback for {first_run_lookback_time} minutes."
        )
        return self._get_now_delayed() - timedelta(minutes=first_run_lookback_time)

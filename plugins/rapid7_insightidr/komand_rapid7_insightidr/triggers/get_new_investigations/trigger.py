import insightconnect_plugin_runtime
import time
from .schema import GetNewInvestigationsInput, GetNewInvestigationsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.constants import TOTAL_SIZE
import json
from datetime import datetime, UTC, timedelta
from typing import Dict, Any, List

DEFAULT_FREQUENCY_SECONDS = 15
INITIAL_LOOKBACK_MINUTES = 10
# set this to be half of the INITIAL_LOOKBACK_MINUTES so the second run doesn't expand the window beyond lookback
API_LATENCY_OVERLAP_MINUTES = 5
MAX_NUMBER_OF_RETRIES = 20

STATE_KEY = "RRNs"
TIME_STATE_KEY = "last_poll_time"


class GetNewInvestigations(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_new_investigations",
            description=Component.DESCRIPTION,
            input=GetNewInvestigationsInput(),
            output=GetNewInvestigationsOutput(),
        )

    @staticmethod
    def get_current_time() -> datetime:
        """Returns current UTC time - extracted for test mocking without adding freezegun dependency to the plugin"""
        return datetime.now(UTC)

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        search = params.get(Input.SEARCH)
        frequency = params.get(Input.FREQUENCY, DEFAULT_FREQUENCY_SECONDS)
        # END INPUT BINDING - DO NOT REMOVE

        # Initialize the trigger starting point & set to dedupe investigations RRNs
        retry_attempts_counter, prev_investigations = 0, set(self.state.get(STATE_KEY, []))

        self.logger.info("Get Investigations: trigger started")
        self.logger.info(f"Investigations search criteria: {search}")

        if last_poll_time := self.state.get(TIME_STATE_KEY):
            self.logger.info(
                f"Detected a container restart, resumming from last poll time: {last_poll_time.isoformat()}"
            )
        else:
            last_poll_time = self.get_current_time() - timedelta(minutes=INITIAL_LOOKBACK_MINUTES)
            self.logger.info(f"Initial poll time set to: '{last_poll_time.isoformat()}'")

        while True:
            # Calculate current time for this iteration (delay 5s to ensure time is safely in past before API indexes)
            current_time = self.get_current_time() - timedelta(seconds=5)
            self.logger.info(
                f"Searching for new investigations from '{last_poll_time.isoformat()}' to '{current_time.isoformat()}'"
            )

            # Get all investigations since last poll time
            # In case of any errors, log the error, wait for the defined frequency, and retry
            try:
                investigations = self.get_investigations(search, last_poll_time, current_time)
            except Exception as error:
                # If max retries reached, raise the error
                if retry_attempts_counter >= MAX_NUMBER_OF_RETRIES:
                    raise error

                # Otherwise, log the error and retry after waiting
                retry_attempts_counter += 1
                self.logger.error("Get Investigations: An error occurred while fetching investigations")
                self.logger.error(error)
                self.logger.info(
                    f"The request will be retried after {frequency} seconds... ({retry_attempts_counter}/{MAX_NUMBER_OF_RETRIES})"
                )
                time.sleep(frequency)
                continue

            # If investigations were found, log total and send them one by one
            # Otherwise, log that no new investigations were found
            if investigations:
                self.logger.info(f"Retrieved total of {len(investigations)} investigations.")
                prev_investigations = self.dedupe_and_send_investigations(investigations, prev_investigations)
            else:
                self.logger.info("No new investigations found.")

            # Update last poll time and reset retry counter for next iteration
            # Overlap window by 5 min to catch late-indexed investigations (IDR indexing is often slow)
            last_poll_time = current_time - timedelta(minutes=API_LATENCY_OVERLAP_MINUTES)
            self.logger.info(f"Checkpoint for next iteration {last_poll_time.isoformat()} to allow for API latency")
            retry_attempts_counter = 0

            # save the state for fallback in case of plugin restart
            self.state[TIME_STATE_KEY] = last_poll_time
            self.state[STATE_KEY] = list(prev_investigations)
            self._save_state()

            # Back off before next iteration
            self.logger.info(f"Sleeping for {frequency} seconds...")
            time.sleep(frequency)

    def get_investigations(
        self, search_query: List[Dict[str, Any]], start_time: datetime, end_time: datetime
    ) -> List[Dict[str, Any]]:
        # Set connection headers for investigations preview and initialize request helper
        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)

        # Define payload for API request
        payload = clean(
            {
                "search": search_query,
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat(),
            }
        )

        # Make initial POST request to search investigations endpoint
        endpoint = Investigations.search_investigation(self.connection.url)
        response = self._call_search_api(request, endpoint, "POST", payload, {"size": TOTAL_SIZE})

        # Collect investigations from the initial response
        investigations = response.get("data", [])
        total_pages = response.get("metadata", {}).get("total_pages", 1)

        # Handle pagination if there are more results than the page size
        if total_pages > 1:
            self.logger.info(f"More pages were found. Total pages: {total_pages}. Fetching remaining pages...")
            for page_index in range(1, total_pages):
                self.logger.info(f"Pulling data from page - ({page_index + 1}/{total_pages})")
                response = self._call_search_api(
                    request, endpoint, "POST", payload, {"size": TOTAL_SIZE, "index": page_index}
                )
                investigations.extend(response.get("data", []))
        return investigations

    def dedupe_and_send_investigations(self, investigations: List[Dict[str, Any]], previous_investigations: set) -> set:
        latest_investigations = set()
        for i, investigation in enumerate(investigations):
            if rrn := investigation.get("rrn"):
                # Track all RRNs from current poll for state management (enables deduplication across restarts)
                latest_investigations.add(rrn)
            else:
                self.logger.warn(f"Investigation {i}: does not have an RRN, skipping deduplication for this investigation.")

            if rrn not in previous_investigations:
                self.send_investigation(investigation, rrn, i)
            else:
                self.logger.info(f"Investigation {i}: Duplicate found and skipped: {rrn}")

        return latest_investigations

    def send_investigation(self, investigation: Dict[str, Any], rrn: str, index: int) -> None:
        self.logger.info(f"Investigation {index}: Found {rrn}")
        self.send({Output.INVESTIGATION: clean(investigation)})

    @staticmethod
    def _call_search_api(
        resource_helper: ResourceHelper,
        endpoint: str,
        method: str,
        payload: Dict[str, Any] = None,
        params: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        response = resource_helper.resource_request(endpoint, method, payload=payload, params=params)
        return json.loads(response.get("resource", "{}"))

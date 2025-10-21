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
INITIAL_LOOKBACK_MINUTES = 1
MAX_NUMBER_OF_RETRIES = 20


class GetNewInvestigations(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_new_investigations",
            description=Component.DESCRIPTION,
            input=GetNewInvestigationsInput(),
            output=GetNewInvestigationsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        search = params.get(Input.SEARCH)
        frequency = params.get(Input.FREQUENCY, DEFAULT_FREQUENCY_SECONDS)
        # END INPUT BINDING - DO NOT REMOVE

        # Initialize the trigger starting point
        retry_attempts_counter = 0
        last_poll_time = datetime.now(UTC) - timedelta(minutes=INITIAL_LOOKBACK_MINUTES)
        self.logger.info("Get Investigations: trigger started")
        self.logger.info(f"Investigations search criteria: {search}")
        self.logger.info(f"Initial poll time set to: '{last_poll_time.isoformat()}'")

        while True:
            # Calculate current time for this iteration (delay by 5 second to avoid overlap) and log search details
            current_time = datetime.now(UTC) - timedelta(seconds=5)
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
                self.logger.info(f"Found total of {len(investigations)} new investigations.")
                for investigation in investigations:
                    self.send_investigation(investigation)
            else:
                self.logger.info("No new investigations found.")

            # Update last poll time and reset retry counter for next iteration
            # Overlap by 1 second to handle IDR API's open time boundaries (exclusive start_time/end_time)
            # This ensures investigations created at exact boundary timestamps are included in the next poll
            last_poll_time = current_time
            retry_attempts_counter = 0

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

    def send_investigation(self, investigation: Dict[str, Any]) -> None:
        self.logger.info(f"Investigation found: {investigation.get('rrn', 'N/A')}")
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

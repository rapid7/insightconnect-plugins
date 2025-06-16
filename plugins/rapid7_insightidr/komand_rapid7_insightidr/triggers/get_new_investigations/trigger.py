import insightconnect_plugin_runtime
import time
from .schema import GetNewInvestigationsInput, GetNewInvestigationsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.constants import TOTAL_SIZE
import json
import datetime


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
        frequency = params.get(Input.FREQUENCY, 15)
        # END INPUT BINDING - DO NOT REMOVE
        self.logger.info("Get Investigations: trigger started", **self.connection.cloud_log_values)

        # Set initial set for storing initial alert_rrn values
        initial_investigations = set()

        # Flag to track the first execution
        first_execution = True

        while True:
            start_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=20)

            data = clean(
                {
                    "search": search,
                    "start_time": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                }
            )
            result = self.make_resource_request(data)
            total_items = result.get("metadata", {}).get("total_items", 0)
            investigations = result.get("data", [])

            # If there are more than 100 results fetch more until all results are stored.
            if total_items > TOTAL_SIZE:
                index = TOTAL_SIZE
                while index < total_items:
                    data["search"]["index"] = index
                    result = self.make_resource_request(data)
                    investigations.extend(result.get("data", []))

            # If not the first iteration send new alerts to output and create new list to compare on next fetch
            if not first_execution:
                for investigation in investigations:
                    investigation_rrn = investigation["rrn"]
                    if investigation_rrn not in initial_investigations:
                        self.send_investigation(investigation)
                initial_investigations = set(investigation["rrn"] for investigation in investigations)
            # For first iteration store alert_rrn's for last 20 minutes for comparison on next fetch.
            else:
                initial_investigations.update(investigation["rrn"] for investigation in investigations)
                first_execution = False

            # Back off before next iteration (sleep for 15 seconds)
            time.sleep(frequency)

    def make_resource_request(self, data):
        try:
            self.connection.headers["Accept-version"] = "investigations-preview"
            request = ResourceHelper(self.connection.headers, self.logger)
            endpoint = Investigations.search_investigation(self.connection.url)
            response = request.resource_request(endpoint, "post", payload=data)
            return self.parse_json_response(response)
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **self.connection.cloud_log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )

    def parse_json_response(self, response):
        try:
            return json.loads(response.get("resource", {}))
        except Exception as error:
            raise PluginException(
                cause="Error: Failed to process investigation results.", assistance=f"Exception returned was {error}"
            )

    def send_investigation(self, investigation: dict):
        self.logger.info(f"Investigation found: {investigation.get('rrn')}", **self.connection.cloud_log_values)
        self.send({Output.INVESTIGATION: clean(investigation)})

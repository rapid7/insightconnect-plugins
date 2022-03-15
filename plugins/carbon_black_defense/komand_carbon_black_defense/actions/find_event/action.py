import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_carbon_black_defense.util.util import Util

from .schema import FindEventInput, FindEventOutput, Input, Output


class FindEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="find_event",
            description="Retrieves all events matching the input search criteria. "
            "Response is a list of events in JSON format."
            "Resulting events are sorted in descending order of time",
            input=FindEventInput(),
            output=FindEventOutput(),
        )

    @Util.retry(tries=6, timeout=60, exceptions=PluginException, backoff_seconds=1)
    def get_enriched_event_status(self, id_):
        enriched_event_search_status = self.connection.get_enriched_event_status(id_)
        if not enriched_event_search_status:
            raise PluginException
        return enriched_event_search_status

    def run(self, params={}):
        device_external_ip = params.get(Input.DEVICE_EXTERNAL_IP)
        process_name = params.get(Input.PROCESS_NAME)
        enriched_event_type = params.get(Input.ENRICHED_EVENT_TYPE)
        process_hash = params.get(Input.PROCESS_HASH)
        device_name = params.get(Input.DEVICE_NAME)
        time_range = params.get(Input.TIME_RANGE)

        criteria = {}

        if device_external_ip:
            criteria["device_external_ip"] = device_external_ip
        if process_name:
            criteria["process_name"] = process_name
        if enriched_event_type:
            criteria["enriched_event_type"] = enriched_event_type
        if process_hash:
            criteria["process_hash"] = process_hash
        if device_name:
            criteria["device_name"] = device_name
        if not criteria:
            raise PluginException(
                cause="No inputs were provided.",
                assistance="At least one input must be provided while configuring this action.",
            )
        id_ = self.connection.get_job_id_for_enriched_event(criteria, None, time_range)

        self.logger.info(f"Got enriched event job ID: {id_}")
        if id_ is None:
            return {Output.RESULTS: None, Output.SUCCESS: False}
        self.get_enriched_event_status(id_)
        response = self.connection.retrieve_results_for_enriched_event(job_id=id_)
        data = insightconnect_plugin_runtime.helper.clean(response)

        return {
            Output.SUCCESS: True,
            Output.RESULTS: data.get("results"),
            Output.APPROXIMATE_UNAGGREGATED: data.get("approximate_unaggregated"),
            Output.NUM_AGGREGATED: data.get("num_aggregated"),
            Output.NUM_AVAILABLE: data.get("num_available"),
            Output.NUM_FOUND: data.get("num_found"),
            Output.CONTACTED: data.get("contacted"),
            Output.COMPLETED: data.get("completed"),
        }

import insightconnect_plugin_runtime
from .schema import (
    MonitorIncidentEventsInput,
    MonitorIncidentEventsOutput,
    MonitorIncidentEventsState,
    Input,
    Output,
    Component,
    State,
)

# Custom imports below
import json

from ...util.util import Util
from typing import List, Dict


INITIAL_HISTORICAL_LOOK_BACK_MS = 1 * 60 * 60 * 1000
DEFAULT_TIME_SORTING_FIELD = "modification_time"


class MonitorIncidentEvents(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_incident_events",
            description=Component.DESCRIPTION,
            input=MonitorIncidentEventsInput(),
            output=MonitorIncidentEventsOutput(),
            state=MonitorIncidentEventsState(),
        )

    @staticmethod
    def get_request_filters(status: str, descriptions: List[str], incident_ids: List[str]) -> List[Dict]:
        filters = []
        if status:
            filters.append({"field": "status", "operator": "eq", "value": status})

        if descriptions:
            filters.append({"field": "description", "operator": "in", "value": descriptions})

        if incident_ids:
            filters.append({"field": "incident_id_list", "operator": "in", "value": incident_ids})

        return filters

    @staticmethod
    def remove_old_and_sort_incident_events(
        incident_events: List[Dict], epoch_cutoff: int, time_sorting_field: str
    ) -> List[Dict]:
        # Discard events < epoch cutoff. This avoid dupes since the XDR API only accepts `>=` and not simply `>`
        cleaned_events_after_cutoff = [
            insightconnect_plugin_runtime.helper.clean_dict(x)
            for x in incident_events
            if x.get(time_sorting_field, -1) > epoch_cutoff
        ]
        cleaned_events_after_cutoff.sort(key=lambda x: x.get(time_sorting_field, -1))
        return cleaned_events_after_cutoff

    def run(self, params={}, state={}):
        # Get all input variables
        status_filter_value = params.get(Input.STATUS)
        descriptions_filter_value = params.get(Input.DESCRIPTIONS)
        incident_id_list_filter_value = params.get(Input.INCIDENT_ID_LIST)
        time_sorting_field = params.get(Input.TIME_SORTING_FIELD, DEFAULT_TIME_SORTING_FIELD)

        # Use the input provided to create the filters for our request
        request_filters = self.get_request_filters(
            status_filter_value, descriptions_filter_value, incident_id_list_filter_value
        )

        self.logger.info(
            f"time sorting field: {time_sorting_field}, request filters: {json.dumps(request_filters, indent=4)}"
        )

        # Figure out the upper and lower time parameters
        now = Util.now_ms()
        last_event_time = state.get(State.LAST_EVENT_TIME)
        if last_event_time is None:
            last_event_time = now - INITIAL_HISTORICAL_LOOK_BACK_MS
        last_event_time = int(last_event_time)

        # Make the request and return the events
        self.logger.info(f"Retrieving Cortex XDR Incident events between {last_event_time} and {now}.")
        events = self.connection.xdr_api.get_incidents(
            from_time=last_event_time, to_time=now, time_sort_field=time_sorting_field, filters=request_filters
        )

        # Remove events with timestamp outside the query range and sort events asc by their modification/creation time
        sorted_events = self.remove_old_and_sort_incident_events(
            incident_events=events, epoch_cutoff=last_event_time, time_sorting_field=time_sorting_field
        )
        # Separate the host identifier values
        for incident in sorted_events:
            incident["hosts"] = Util.split_list_values(incident.get("hosts", []), ":")
        self.logger.info(f"Finished retrieving {len(sorted_events)} new incident events this iteration.")
        return {Output.EVENTS: sorted_events}, {State.LAST_EVENT_TIME: str(now)}

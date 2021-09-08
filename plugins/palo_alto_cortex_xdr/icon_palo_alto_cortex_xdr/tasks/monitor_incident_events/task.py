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
    def get_request_filters(
        status: str, alert_source: List[str], descriptions: List[str], incident_ids: List[str]
    ) -> List[Dict]:
        filters = []
        if status is not None and len(status) > 0:
            filters.append({"field": "status", "operator": "eq", "value": status})

        if alert_source is not None and len(alert_source) > 0:
            filters.append({"field": "alert_sources", "operator": "eq", "value": alert_source})

        if descriptions is not None and len(descriptions) > 0:
            filters.append({"field": "description", "operator": "in", "value": descriptions})

        if incident_ids is not None and len(incident_ids) > 0:
            filters.append({"field": "incident_id_list", "operator": "in", "value": incident_ids})

        return filters

    @staticmethod
    def remove_old_and_sort_incident_events(
        incident_events: List[Dict], epoch_cutoff: int, time_sorting_field: str
    ) -> List[Dict]:
        events_after_cutoff = [x for x in incident_events if x.get(time_sorting_field, -1) > epoch_cutoff]
        events_after_cutoff.sort(key=lambda x: x.get(time_sorting_field, -1))
        return events_after_cutoff

    def run(self, params={}, state={}):
        # Get all input variables
        status_filter_value = params.get(Input.STATUS, None)
        alert_source_filter_value = params.get(Input.ALERT_SOURCE, None)
        descriptions_filter_value = params.get(Input.DESCRIPTIONS, None)
        incident_id_list_filter_value = params.get(Input.INCIDENT_ID_LIST, None)

        # Use the input provided to create the filters for our request
        request_filters = self.get_request_filters(
            status_filter_value, alert_source_filter_value, descriptions_filter_value, incident_id_list_filter_value
        )

        self.logger.info(f"request filters: {json.dumps(request_filters, indent=4)}")

        # Get the input that let's us know if we are sorting events by modification or creation time
        time_sorting_field = params.get(Input.TIME_SORTING_FIELD, DEFAULT_TIME_SORTING_FIELD)

        self.logger.info(f"using '{time_sorting_field}' field to filter and sort incident events.")

        # Figure out the upper and lower time parameters
        now = Util.now_ms()
        last_event_time = state.get(State.LAST_EVENT_TIME, None)
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

        self.logger.info(f"Finished retrieving {len(sorted_events)} new incident events this iteration.")
        # XDRs API only allows greater-than-equals and not greater-than. Therefore, add 1 ms to 'now' so we don't ask
        # for 'now' again on the next run.
        return {Output.EVENTS: sorted_events}, {State.LAST_EVENT_TIME: str(now + 1)}

import insightconnect_plugin_runtime
from .schema import (
    GetEventsByTypeInput,
    GetEventsByTypeOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from komand_sentinelone.util.helper import clean


class GetEventsByType(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_events_by_type",
            description=Component.DESCRIPTION,
            input=GetEventsByTypeInput(),
            output=GetEventsByTypeOutput(),
        )

    def run(self, params={}):
        limit = params.get(Input.LIMIT)
        get_all_results = True

        parameters = {
            "queryId": params.get(Input.QUERYID),
            "subQuery": params.get(Input.SUBQUERY),
            "limit": 1000,
        }

        response = clean(self.connection.client.get_events(clean(parameters), get_all_results))
        events_data = clean(
            [event for event in response.get("data", []) if event.get("eventType") == params.get(Input.EVENTTYPE)]
        )

        return {
            Output.EVENTS: (events_data[0:limit] if limit and limit in range(1, 1000) else events_data),
            **clean({Output.ERRORS: response.get("errors", [])}),
        }

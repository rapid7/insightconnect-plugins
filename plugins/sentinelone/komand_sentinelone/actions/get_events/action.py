import insightconnect_plugin_runtime
from .schema import GetEventsInput, GetEventsOutput, Input, Output, Component
from komand_sentinelone.util.helper import clean

# Custom imports below


class GetEvents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_events",
            description=Component.DESCRIPTION,
            input=GetEventsInput(),
            output=GetEventsOutput(),
        )

    def run(self, params={}):
        limit = params.get(Input.LIMIT)
        get_all_results = False

        params = {
            "queryId": params.get(Input.QUERYID),
            "subQuery": params.get(Input.SUBQUERY),
            "limit": limit if limit and limit in range(1, 1000) else 1000,
        }

        if not (limit and limit in range(1, 1000)):
            get_all_results = True
        response = clean(self.connection.client.get_events(clean(params), get_all_results))
        return {
            Output.EVENTS: response.get("data", []),
            **clean({Output.ERRORS: response.get("errors", [])}),
        }

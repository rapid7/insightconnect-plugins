import insightconnect_plugin_runtime
from .schema import GetEventsByTypeInput, GetEventsByTypeOutput, Input, Output, Component
# Custom imports below


class GetEventsByType(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_events_by_type',
                description=Component.DESCRIPTION,
                input=GetEventsByTypeInput(),
                output=GetEventsByTypeOutput())

    def run(self, params={}):
        limit = params.get(Input.LIMIT)
        sub_query = params.get(Input.SUB_QUERY)
        get_all_results = False

        params = {
            "queryId": params.get(Input.QUERY_ID)
        }

        if limit:
            params["limit"] = limit
        else:
            get_all_results = True
        if sub_query:
            params["subQuery"] = sub_query

        return {Output.RESPONSE: self.connection.get_events(
            params,
            get_all_results,
            event_type=params.get(Input.EVENT_TYPE),
        )}

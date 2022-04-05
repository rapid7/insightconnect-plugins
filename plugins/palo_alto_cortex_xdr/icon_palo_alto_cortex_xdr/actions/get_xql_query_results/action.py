import insightconnect_plugin_runtime
from .schema import GetXqlQueryResultsInput, GetXqlQueryResultsOutput, Input, Output, Component

# Custom imports below


class GetXqlQueryResults(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_xql_query_results",
            description=Component.DESCRIPTION,
            input=GetXqlQueryResultsInput(),
            output=GetXqlQueryResultsOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        tenants = params.get(Input.TENANTS)
        from_ = params.get(Input.START_TIME)
        to = params.get(Input.END_TIME)
        limit = params.get(Input.LIMIT)
        execution_id = self.connection.xdr_api.start_xql_query(query, tenants, from_, to)
        output = insightconnect_plugin_runtime.helper.clean(
            self.connection.xdr_api.get_xql_query_results(execution_id, limit)
        )
        return {Output.REPLY: output}

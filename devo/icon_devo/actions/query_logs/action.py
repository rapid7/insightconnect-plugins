import insightconnect_plugin_runtime
from .schema import QueryLogsInput, QueryLogsOutput, Input, Output, Component
# Custom imports below


class QueryLogs(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query_logs',
                description=Component.DESCRIPTION,
                input=QueryLogsInput(),
                output=QueryLogsOutput())

    def run(self, params={}):
        query = params.get(Input.QUERY)
        from_date = params.get(Input.FROM_DATE)
        to_date = params.get(Input.TO_DATE)
        output = self.connection.api.query(query, from_date, to_date)
        return {Output.RESULTS: insightconnect_plugin_runtime.helper.clean(output)}

import insightconnect_plugin_runtime
from .schema import QueryLogsInput, QueryLogsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class QueryLogs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query_logs", description=Component.DESCRIPTION, input=QueryLogsInput(), output=QueryLogsOutput()
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        query = self._add_limit_to_query(query)

        from_date = params.get(Input.FROM_DATE)
        to_date = params.get(Input.TO_DATE)
        output, _ = self.connection.api.query(query, from_date, to_date)
        if output:
            return {Output.RESULTS: insightconnect_plugin_runtime.helper.clean(output)}

        raise PluginException(PluginException.Preset.UNKNOWN)

    def _add_limit_to_query(self, query: str) -> str:
        if not "limit" in query.lower():
            self.logger.info("Adding limit to query.")
            query += " limit 1000"
            self.logger.info(f"Query: {query}")
        return query

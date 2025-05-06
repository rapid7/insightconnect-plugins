import insightconnect_plugin_runtime

from komand_sql.connection import connection

# Custom imports below
from komand_sql.util.util import generate_results

from .schema import Input, Output, QueryInput, QueryOutput


class Query(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query",
            description="SQL query",
            input=QueryInput(),
            output=QueryOutput(),
        )

    def run(self, params={}):
        with connection.SQLConnection(self.connection.conn_str) as s:
            try:
                results = generate_results(
                    s,
                    params.get(Input.QUERY),
                    dict(params.get(Input.PARAMETERS)),
                    self.logger,
                )
            finally:
                s.session.close()

        return {
            Output.STATUS: results["status"],
            Output.RESULTS: results.get("results", []),
            Output.HEADER: results.get("header", []),
        }

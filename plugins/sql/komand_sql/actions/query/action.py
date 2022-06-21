import komand
from .schema import QueryInput, QueryOutput, Input, Output

# Custom imports below
from komand_sql.util.util import generate_results
from komand_sql.connection import connection


class Query(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query", description="SQL query", input=QueryInput(), output=QueryOutput()
        )

    def run(self, params={}):
        with connection.SQLConnection(self.connection.conn_str) as s:
            try:
                results = generate_results(
                    self.connection.type,
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

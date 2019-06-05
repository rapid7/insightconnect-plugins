import komand
from .schema import QueryInput, QueryOutput
# Custom imports below
from komand_sql.util.util import generate_results


class Query(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query',
                description='SQL query',
                input=QueryInput(),
                output=QueryOutput())

    def run(self, params={}):
        query = params.get("query")
        parameters = dict(params.get("parameters"))

        conn = self.connection.connection
        conn_type = self.connection.params["type"]

        results = generate_results(conn_type, conn, query, parameters, self.logger)

        return results


    def test(self, params={}):
        session = self.connection.connection.session
        if session:
            return {"status": "operation success"}
        else:
            raise Exception("Connection was not active. Please check your connection settings.")


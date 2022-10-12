import insightconnect_plugin_runtime
import time
from .schema import GetQueryResultsInput, GetQueryResultsOutput, Input, Output, Component

# Custom imports below
from ...util.util import Util


class GetQueryResults(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_query_results",
            description=Component.DESCRIPTION,
            input=GetQueryResultsInput(),
            output=GetQueryResultsOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        tenants = params.get(Input.TENANTS)
        limit = params.get(Input.LIMIT)
        interval = abs(params.get(Input.FREQUENCY, 5))

        end_time = Util.now_ms() - interval * 1000

        self.logger.info("Initializing Get Query Results trigger for the Palo Alto Cortex XDR plugin.")

        while True:
            start_time = Util.now_ms()
            execution_id = self.connection.xdr_api.start_xql_query(query, tenants, end_time, start_time)
            query_results = insightconnect_plugin_runtime.helper.clean(
                self.connection.xdr_api.get_xql_query_results(execution_id, limit)
            )
            if any((query_results.get("results", {}).get("data"), query_results.get("results", {}).get("stream_id"))):
                self.send({Output.REPLY: query_results})
            else:
                self.logger.info("No query results found.")
            self.logger.info(f"Sleeping for {interval} seconds...\n")
            end_time = Util.now_ms()
            time.sleep(interval)

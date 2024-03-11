import insightconnect_plugin_runtime

from .schema import Component, Input, Output, QueryEndpointInput, QueryEndpointOutput

# Custom imports below


class QueryEndpoint(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query_endpoint",
            description=Component.DESCRIPTION,
            input=QueryEndpointInput(),
            output=QueryEndpointOutput(),
        )

    def run(self, params={}):
        hostname = params.get(Input.HOSTNAME)

        result = self.connection.ers.get_endpoint_by_name(hostname)
        try:
            if result == "Not Found":
                self.logger.error("Endpoint was not found")
                return {Output.ERS_ENDPOINT: {}}
            results = result["ERSEndPoint"]
        except KeyError:
            self.logger.error(f"No endpoint key in results, {result}")
            raise
        except Exception as error:
            self.logger.error(error)
            self.logger.error(f"Query results, {result}")
            self.logger.error(f"Hostname, {hostname}")
            raise

        return {Output.ERS_ENDPOINT: results}

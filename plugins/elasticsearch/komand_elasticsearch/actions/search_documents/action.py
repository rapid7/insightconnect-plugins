import insightconnect_plugin_runtime
from .schema import SearchDocumentsInput, SearchDocumentsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SearchDocuments(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_documents",
            description=Component.DESCRIPTION,
            input=SearchDocumentsInput(),
            output=SearchDocumentsOutput(),
        )

    def run(self, params={}):
        index = params.get(Input.INDEX)
        routing = params.get(Input.ROUTING)
        query = params.get(Input.QUERY)

        params = {}
        if routing:
            params["routing"] = routing

        results = self.connection.client.search_documents(index, query, params)
        if not results:
            raise PluginException(
                cause="Document search not run. ", assistance="Please check provided data and try again."
            )

        if not results["hits"]["max_score"]:
            results["hits"]["max_score"] = 0

        for hit in results["hits"]["hits"]:
            if "_score" not in hit or hit["_score"] is None:
                hit["_score"] = 0
                self.logger.info("One or most results lack a relevance score, assuming 0")

        return insightconnect_plugin_runtime.helper.clean(
            {
                Output.SHARDS: results["_shards"],
                Output.HITS: results["hits"],
                Output.TOOK: results["took"],
                Output.TIMED_OUT: results["timed_out"],
            }
        )

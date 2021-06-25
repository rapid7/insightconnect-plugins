import insightconnect_plugin_runtime
import time
from .schema import PollDocumentsInput, PollDocumentsOutput, Input, Component

# Custom imports below


class PollDocuments(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="poll_documents",
            description=Component.DESCRIPTION,
            input=PollDocumentsInput(),
            output=PollDocumentsOutput(),
        )

    def run(self, params={}):
        frequency = params.get(Input.FREQUENCY, 60)
        index = params.get(Input.INDEX)
        routing = params.get(Input.ROUTING)
        query = params.get(Input.QUERY)

        old_d = {}
        params = {}
        if routing:
            params["routing"] = routing

        while True:
            try:
                results = self.connection.client.search_documents(index, query, params)
            except:
                self.logger.error(f"Poll Documents: poll failed... trying again in {frequency} seconds.")
                time.sleep(frequency)
                continue

            if not results or "hits" not in results:
                self.logger.error(f"Poll Documents: poll failed... trying again in {frequency} seconds.")
                time.sleep(frequency)
                continue

            hits = []
            for hit in results["hits"]["hits"]:
                if hit["_score"] is None or "_score" not in hit:
                    hit["_score"] = 0
                    self.logger.info("One or most results lack a relevance score, assuming 0")
                hits.append(hit)
                if hit.get("_version"):
                    if hit["_id"] not in old_d:
                        old_d[hit["_id"]] = [hit["_version"]]
                    else:
                        if hit["_version"] not in old_d[hit["_id"]]:
                            old_d[hit["_id"]].append(hit["_version"])

            if not hits:
                time.sleep(frequency)
                continue

            self.send({"hits": hits})
            time.sleep(frequency)

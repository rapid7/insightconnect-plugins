import komand
import json
from .schema import SearchHashesInput, SearchHashesOutput


class SearchHashes(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_hashes",
            description="This action is used to search for data related to hashes of a specified type",
            input=SearchHashesInput(),
            output=SearchHashesOutput(),
        )

    def run(self, params={}):
        try:
            results = self.connection.client.search_hashes(**params)
            return json.loads(results._req_response._content.decode("utf-8"))
        except Exception as e:
            self.logger.error("Error: " + str(e))

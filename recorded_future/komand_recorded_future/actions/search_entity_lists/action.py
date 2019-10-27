import komand
import requests
from .schema import SearchEntityListsInput, SearchEntityListsOutput


class SearchEntityLists(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_entity_lists",
            description="This action is used to perform a freetext search across all Recorded Future entity types (IP address, domain, hash, malware, and vulnerability)",
            input=SearchEntityListsInput(),
            output=SearchEntityListsOutput(),
        )

    def run(self, params={}):
        try:
            query_params = params
            query_headers = {"X-RFToken": self.connection.token}
            results = requests.get(
                "https://api.recordedfuture.com/v2/entitylist/search",
                params=query_params,
                headers=query_headers,
            )
            return results.json()
        except Exception as e:
            self.logger.error("Error: " + str(e))

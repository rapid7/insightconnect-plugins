import komand
import requests
from .schema import SearchInput, SearchOutput


class Search(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='Search GitHub for data',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        try:
            search_type = params.get("search_type").lower()
            search_params = {"q": params.get("query")}
            results = requests.get(
                "https://api.github.com/search/" + search_type,
                params=search_params,
                auth=self.connection.basic_auth
            )
            return {"results": results.json()}
        except Exception as e:
            self.logger.error("Search failed. Error: " + str(e))

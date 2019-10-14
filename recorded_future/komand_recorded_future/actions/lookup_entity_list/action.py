import komand
import requests
from .schema import LookupEntityListInput, LookupEntityListOutput


class LookupEntityList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_entity_list",
            description="This action is used to fetch a specified entity list by ID",
            input=LookupEntityListInput(),
            output=LookupEntityListOutput(),
        )

    def run(self, params={}):
        try:
            list_id = params.get("entity_list_id")
            query_headers = {"X-RFToken": self.connection.token}
            query_url = "https://api.recordedfuture.com/v2/entitylist/" + list_id
            results = requests.get(query_url, headers=query_headers)
            return results.json()
        except Exception as e:
            self.logger.error("Error: " + str(e))

import komand
import json
from .schema import SearchIPAddressesInput, SearchIPAddressesOutput


class SearchIPAddresses(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_IP_addresses",
            description="This action is used to query for data related to a specified IP range",
            input=SearchIPAddressesInput(),
            output=SearchIPAddressesOutput(),
        )

    def run(self, params={}):
        try:
            results = self.connection.client.search_ips(**params)
            return json.loads(results._req_response._content.decode("utf-8"))
        except Exception as e:
            self.logger.error("Error: " + str(e))

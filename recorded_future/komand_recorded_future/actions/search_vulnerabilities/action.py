import komand
import json
from .schema import SearchVulnerabilitiesInput, SearchVulnerabilitiesOutput


class SearchVulnerabilities(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_vulnerabilities",
            description="This action is used to search for data related to vulnerabilities",
            input=SearchVulnerabilitiesInput(),
            output=SearchVulnerabilitiesOutput(),
        )

    def run(self, params={}):
        try:
            results = self.connection.client.search_vulnerabilities(**params)
            return json.loads(results._req_response._content.decode("utf-8"))
        except Exception as e:
            self.logger.error("Error: " + str(e))

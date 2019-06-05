import komand
import json
from .. import demo_test
from .schema import SearchDomainsInput, SearchDomainsOutput


class SearchDomains(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_domains',
                description='This action is used to search for results related to a specific parent domain',
                input=SearchDomainsInput(),
                output=SearchDomainsOutput())

    def run(self, params={}):
        try:
            results = self.connection.client.search_domains(**params)
            return json.loads(results._req_response._content.decode("utf-8"))
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        return demo_test.demo_test(self.connection.token, self.logger)

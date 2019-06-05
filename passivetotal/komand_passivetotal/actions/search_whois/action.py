import komand
from .schema import SearchWhoisInput, SearchWhoisOutput
# Custom imports below
from komand_passivetotal.util import util


class SearchWhois(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_whois',
                description='Search WHOIS [https://api.passivetotal.org/api/docs/#api-WHOIS-GetV2WhoisSearchQueryField]',
                input=SearchWhoisInput(),
                output=SearchWhoisOutput())

    def run(self, params={}):
        field = params.get('field')
        query = params['query']
        self.logger.info('Query and field: %s %s', query, field)
        results = self.connection.whois.search_whois_by_field(query=query, field=field)
        if results:
            results = util.clean_dict_recursive(results)

        return {'found': not not results, 'record': results}

    def test(self):
        # TODO: Implement test function
        return {}

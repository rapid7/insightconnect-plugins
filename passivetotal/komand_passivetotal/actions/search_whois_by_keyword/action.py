import komand
from .schema import SearchWhoisByKeywordInput, SearchWhoisByKeywordOutput
# Custom imports below
from komand_passivetotal.util import util


class SearchWhoisByKeyword(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_whois_by_keyword',
                description='Search WHOIS By keyword',
                input=SearchWhoisByKeywordInput(),
                output=SearchWhoisByKeywordOutput())

    def run(self, params={}):
        query = params['query']
        self.logger.info('Query  %s', query)
        results = self.connection.whois.search_keyword(query=query)
        if results and 'results' in results:
            self.logger.debug('Returned: %s', results)
            results = util.clean_dict_recursive(results)
            results = results['results']

        count = len(results)
        return {'count': count, 'results': results}

    def test(self):
        # TODO: Implement test function
        return {}

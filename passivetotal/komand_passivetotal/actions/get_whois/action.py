import komand
from .schema import GetWhoisInput, GetWhoisOutput
# Custom imports below
from komand_passivetotal.util import util


class GetWhois(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_whois',
                description='WHOIS Query [https://api.passivetotal.org/api/docs/#api-WHOIS-GetV2WhoisQuery]',
                input=GetWhoisInput(),
                output=GetWhoisOutput())

    def run(self, params={}):
        compact_record = not not params.get('compact_record')
        query = params['query']
        self.logger.info('Query: %s', query)
        results = self.connection.whois.get_whois_details(query=query, compact_record=compact_record)
        if results:
            results = util.clean_dict_recursive(results)

        return {'found': not not results, 'record': results}

    def test(self):
        # TODO: Implement test function
        return {}

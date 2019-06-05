import komand
from .schema import TicketSearchInput, TicketSearchOutput
# Custom imports below


class TicketSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ticket_search',
                description='Gets tickets matching defined parameters',
                input=TicketSearchInput(),
                output=TicketSearchOutput())

    def run(self, params={}):
        args = {
            'Queue': params.get('queue'),
            'order': params.get('order'),
            'raw_query': params.get('raw_query')
        }
        query_args = komand.helper.clean_dict(args)
        keywords = params.get('keywords')
        if keywords:
            query_args = dict(list(query_args.items()) + list(keywords.items()))
            results = self.connection.tracker.search(**query_args)
        else:
            results = self.connection.tracker.search(**query_args)
        return {'Tickets': results}

    def test(self):
        # TODO: Implement test function
        return {}

import komand
from .schema import TicketLinksInput, TicketLinksOutput
# Custom imports below


class TicketLinks(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ticket_links',
                description='Gets the ticket links for a single ticket',
                input=TicketLinksInput(),
                output=TicketLinksOutput())

    def run(self, params={}):
        ticket_links = self.connection.tracker.get_links(params['ticket_id'])
        return ticket_links

    def test(self):
        # TODO: Implement test function
        return {}

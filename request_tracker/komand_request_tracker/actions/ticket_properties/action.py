import komand
from .schema import TicketPropertiesInput, TicketPropertiesOutput
# Custom imports below


class TicketProperties(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ticket_properties',
                description='Gets the data for a single ticket, not including the history and comments',
                input=TicketPropertiesInput(),
                output=TicketPropertiesOutput())

    def run(self, params={}):
        ticket = self.connection.tracker.get_ticket(params['ticket_id'])
        return {'Ticket': ticket}

    def test(self):
        # TODO: Implement test function
        return {}

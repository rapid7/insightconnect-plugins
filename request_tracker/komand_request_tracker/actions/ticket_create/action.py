import komand
from .schema import TicketCreateInput, TicketCreateOutput
# Custom imports below


class TicketCreate(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ticket_create',
                description='Creates a new ticket',
                input=TicketCreateInput(),
                output=TicketCreateOutput())

    def run(self, params={}):
        queue = params.get('queue')
        keywords = params.get('keywords', {})
        keywords = komand.helper.clean_dict(keywords)
        if queue:
            ticket_id = self.connection.tracker.create_ticket(Queue=queue, **keywords)
        else:
            ticket_id = self.connection.tracker.create_ticket(**keywords)

        return {'TicketId': ticket_id}

    def test(self):
        # TODO: Implement test function
        return {}

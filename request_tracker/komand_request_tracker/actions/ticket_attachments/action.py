import komand
from .schema import TicketAttachmentsInput, TicketAttachmentsOutput
# Custom imports below
from collections import namedtuple


class TicketAttachments(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ticket_attachments',
                description='Gets a list of all attachments related to the ticket',
                input=TicketAttachmentsInput(),
                output=TicketAttachmentsOutput())

    def run(self, params={}):
        ticket_id = params['ticket_id']
        resp = self.connection.tracker.get_attachments(ticket_id)
        attachments = [dict(Attachment(*x)._asdict()) for x in resp]
        return {'Attachments': attachments}

    def test(self):
        # TODO: Implement test function
        return {}

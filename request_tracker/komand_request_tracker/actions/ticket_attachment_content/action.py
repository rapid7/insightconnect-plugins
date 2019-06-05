import komand
from .schema import TicketAttachmentContentInput, TicketAttachmentContentOutput
# Custom imports below


class TicketAttachmentContent(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ticket_attachment_content',
                description='Gets the metadata and content of a specific attachment',
                input=TicketAttachmentContentInput(),
                output=TicketAttachmentContentOutput())

    def run(self, params={}):
        ticket_id = params['ticket_id']
        attachment_id = params['attachment_id']
        content = self.connection.tracker.get_attachment_content(ticket_id, attachment_id)
        try:
            content = content.decode('utf-8')
        except:
            content = ''

        return {'Content': content}

    def test(self):
        # TODO: Implement test function
        return {}

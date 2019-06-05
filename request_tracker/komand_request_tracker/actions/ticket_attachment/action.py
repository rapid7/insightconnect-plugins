import komand
from .schema import TicketAttachmentInput, TicketAttachmentOutput
# Custom imports below


class TicketAttachment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ticket_attachment',
                description='Gets the metadata and content of a specific attachment',
                input=TicketAttachmentInput(),
                output=TicketAttachmentOutput())

    def run(self, params={}):
        ticket_id = params['ticket_id']
        attachment_id = params['attachment_id']
        attachment = self.connection.tracker.get_attachment(ticket_id, attachment_id)
        attachment['Transaction'] = int(attachment['Transaction'])
        attachment['Parent'] = int(attachment['Parent'])
        attachment['id'] = int(attachment['id'])
        # validation error is raised when content is empty
        try:
            attachment['Content'] = attachment['Content'].decode('utf-8')
        except:
            attachment['Content'] = ''

        return attachment

    def test(self):
        # TODO: Implement test function
        return {}

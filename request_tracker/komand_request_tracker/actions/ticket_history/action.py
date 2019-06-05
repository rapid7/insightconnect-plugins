import komand
from .schema import TicketHistoryInput, TicketHistoryOutput
# Custom imports below
from komand_request_tracker.util import utils


class TicketHistory(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ticket_history',
                description='Gets a list of all the history items for a given ticket',
                input=TicketHistoryInput(),
                output=TicketHistoryOutput())

    def run(self, params={}):
        ticket_id = params['ticket_id']
        history = self.connection.tracker.get_history(ticket_id)
        # 'Attachments' holds list of pairs (attachment_id,filename_with_size).
        for entry in history:
            attachments = utils.attachments_to_dict(entry)
            entry['Attachments'] = attachments

        return {'History': history}

    def test(self):
        # TODO: Implement test function
        return {}

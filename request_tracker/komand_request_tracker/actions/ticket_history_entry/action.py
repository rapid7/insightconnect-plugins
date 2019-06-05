import komand
from .schema import TicketHistoryEntryInput, TicketHistoryEntryOutput
# Custom imports below
from komand_request_tracker.util import utils

class TicketHistoryEntry(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ticket_history_entry',
                description='Gets the history information for a single history item. Note that the history item must actually correspond to the ticket',
                input=TicketHistoryEntryInput(),
                output=TicketHistoryEntryOutput())

    def run(self, params={}):
        ticket_id = params['ticket_id']
        history_id = params['history_id']
        history = self.connection.tracker.get_history(ticket_id, history_id)
        for entry in history:
            attachments = utils.attachments_to_dict(entry)
            entry['Attachments'] = attachments

        return {'History': history}

    def test(self):
        # TODO: Implement test function
        return {}

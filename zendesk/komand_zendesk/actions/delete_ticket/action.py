import komand
from .schema import DeleteTicketInput, DeleteTicketOutput
# Custom imports below
import json
import zenpy

class DeleteTicket(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_ticket',
                description='Delete ticket',
                input=DeleteTicketInput(),
                output=DeleteTicketOutput())

    def run(self, params={}):
        try:
          client = self.connection.client
          ticket = client.tickets(id=params.get('ticket_id'))
          deleted = client.tickets.delete(ticket)
          return {"status": True}
        except zenpy.lib.exception.APIException as e:
          self.logger.debug(e)
          return {"status": False}

    def test(self):
      try:
        test = self.connection.client.users.me().email
        return { 'success': test }
      except:
        raise

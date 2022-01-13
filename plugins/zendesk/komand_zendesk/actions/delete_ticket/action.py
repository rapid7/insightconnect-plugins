import insightconnect_plugin_runtime
from .schema import DeleteTicketInput, DeleteTicketOutput, Input, Output

# Custom imports below
import json
import zenpy


class DeleteTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_ticket",
            description="Delete ticket",
            input=DeleteTicketInput(),
            output=DeleteTicketOutput(),
        )

    def run(self, params={}):
        try:
            client = self.connection.client
            ticket = client.tickets(id=params.get(Input.TICKET_ID))
            deleted = client.tickets.delete(ticket)
            return {Output.STATUS: True}
        except zenpy.lib.exception.APIException as e:
            self.logger.debug(e)
            return {Output.STATUS: False}

    def test(self):
        try:
            test = self.connection.client.users.me().email
            return {"success": test}
        except:
            raise

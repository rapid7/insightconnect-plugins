import insightconnect_plugin_runtime
from .schema import DeleteTicketInput, DeleteTicketOutput, Input, Output

# Custom imports below


class DeleteTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_ticket",
            description="Delete ticket",
            input=DeleteTicketInput(),
            output=DeleteTicketOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.TICKET_ID)

        try:
            ticket = self.connection.client.tickets(id=identifier)
            self.connection.client.tickets.delete(ticket)
            return {Output.STATUS: True}
        except Exception as error:
            self.logger.debug(error)
            return {Output.STATUS: False}

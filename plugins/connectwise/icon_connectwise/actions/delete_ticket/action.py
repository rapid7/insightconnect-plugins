import insightconnect_plugin_runtime
from .schema import DeleteTicketInput, DeleteTicketOutput, Input, Output, Component

# Custom imports below


class DeleteTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_ticket",
            description=Component.DESCRIPTION,
            input=DeleteTicketInput(),
            output=DeleteTicketOutput(),
        )

    def run(self, params: dict = None) -> dict:
        return {Output.SUCCESS: self.connection.api_client.delete_ticket(params.get(Input.TICKET_ID))}

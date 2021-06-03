import insightconnect_plugin_runtime
from .schema import UpdateTicketInput, UpdateTicketOutput, Input, Output, Component

# Custom imports below


class UpdateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket",
            description=Component.DESCRIPTION,
            input=UpdateTicketInput(),
            output=UpdateTicketOutput(),
        )

    def run(self, params={}):
        return {Output.RESULT: self.connection.client.ticket_action("PUT", params, params.get(Input.RFC_NUMBER))}

import insightconnect_plugin_runtime
from .schema import CloseTicketInput, CloseTicketOutput, Input, Output, Component

# Custom imports below


class CloseTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_ticket", description=Component.DESCRIPTION, input=CloseTicketInput(), output=CloseTicketOutput()
        )

    def run(self, params={}):
        return {
            Output.RESULT: self.connection.client.ticket_action("PUT", {"closed": params}, params.get(Input.RFC_NUMBER))
        }

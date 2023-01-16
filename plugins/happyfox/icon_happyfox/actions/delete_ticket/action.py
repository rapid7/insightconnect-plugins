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

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.api.delete_ticket(
                params.get(Input.TICKETID), {"staff_id": params.get(Input.STAFFID)}
            )
        }

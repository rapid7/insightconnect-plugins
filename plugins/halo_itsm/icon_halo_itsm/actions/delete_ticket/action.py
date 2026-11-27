import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument
from .schema import DeleteTicketInput, DeleteTicketOutput, Input, Output, Component


class DeleteTicket(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_ticket",
            description=Component.DESCRIPTION,
            input=DeleteTicketInput(),
            output=DeleteTicketOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ticket_id = params.get(Input.TICKET_ID)
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info(f"Deleting ticket with ID: {ticket_id}")
        self.connection.client.delete_ticket(ticket_id)

        return {Output.SUCCESS: True}

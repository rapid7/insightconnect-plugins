import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument
from .schema import GetTicketInput, GetTicketOutput, Input, Output, Component
from icon_halo_itsm.util.helpers import clean_ticket


class GetTicket(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_ticket",
            description=Component.DESCRIPTION,
            input=GetTicketInput(),
            output=GetTicketOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ticket_id = params.get(Input.TICKET_ID)
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info(f"Retrieving ticket with ID: {ticket_id}")
        result = self.connection.client.get_ticket(ticket_id)

        return {Output.TICKET: clean_ticket(result)}

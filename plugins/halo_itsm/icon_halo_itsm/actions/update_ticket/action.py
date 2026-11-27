import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument
from .schema import UpdateTicketInput, UpdateTicketOutput, Input, Output, Component
from icon_halo_itsm.util.helpers import clean_ticket


class UpdateTicket(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket",
            description=Component.DESCRIPTION,
            input=UpdateTicketInput(),
            output=UpdateTicketOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ticket_id = params.get(Input.TICKET_ID)
        agent_id = params.get(Input.AGENT_ID)
        category_1 = params.get(Input.CATEGORY_1)
        category_2 = params.get(Input.CATEGORY_2)
        details = params.get(Input.DETAILS)
        impact = params.get(Input.IMPACT)
        priority_id = params.get(Input.PRIORITY_ID)
        status_id = params.get(Input.STATUS_ID)
        summary = params.get(Input.SUMMARY)
        urgency = params.get(Input.URGENCY)
        # END INPUT BINDING - DO NOT REMOVE

        ticket_data = {}

        if summary:
            ticket_data["summary"] = summary
        if details:
            ticket_data["details"] = details
        if status_id:
            ticket_data["status_id"] = status_id
        if priority_id:
            ticket_data["priority_id"] = priority_id
        if agent_id:
            ticket_data["agent_id"] = agent_id
        if category_1:
            ticket_data["category_1"] = category_1
        if category_2:
            ticket_data["category_2"] = category_2
        if impact:
            ticket_data["impact"] = impact
        if urgency:
            ticket_data["urgency"] = urgency

        self.logger.info(f"Updating ticket with ID: {ticket_id}")
        result = self.connection.client.update_ticket(ticket_id, ticket_data)

        return {Output.TICKET: clean_ticket(result)}

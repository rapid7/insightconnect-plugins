import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument
from .schema import CreateTicketInput, CreateTicketOutput, Input, Output, Component
from icon_halo_itsm.util.helpers import clean_ticket


class CreateTicket(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket",
            description=Component.DESCRIPTION,
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        agent_id = params.get(Input.AGENT_ID)
        category_1 = params.get(Input.CATEGORY_1)
        category_2 = params.get(Input.CATEGORY_2)
        client_id = params.get(Input.CLIENT_ID)
        details = params.get(Input.DETAILS)
        impact = params.get(Input.IMPACT)
        priority_id = params.get(Input.PRIORITY_ID)
        site_id = params.get(Input.SITE_ID)
        status_id = params.get(Input.STATUS_ID)
        summary = params.get(Input.SUMMARY)
        tickettype_id = params.get(Input.TICKETTYPE_ID)
        urgency = params.get(Input.URGENCY)
        user_id = params.get(Input.USER_ID)
        # END INPUT BINDING - DO NOT REMOVE

        optional_fields = {
            "details": details,
            "agent_id": agent_id,
            "category_1": category_1,
            "category_2": category_2,
            "client_id": client_id,
            "impact": impact,
            "priority_id": priority_id,
            "site_id": site_id,
            "status_id": status_id,
            "urgency": urgency,
            "user_id": user_id,
        }
        # Workflows send 0 or an empty value for what they leave unset; Halo must not receive those
        ticket_data = {"summary": summary, "tickettype_id": tickettype_id}
        ticket_data.update({key: value for key, value in optional_fields.items() if value})

        self.logger.info("Creating ticket")
        result = self.connection.client.create_ticket(ticket_data)

        return {Output.TICKET: clean_ticket(result)}

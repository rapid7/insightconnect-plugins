"""Update Ticket action for TeamDynamix InsightConnect plugin."""

import insightconnect_plugin_runtime
from .schema import UpdateTicketInput, UpdateTicketOutput, Input, Output, Component


class UpdateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket",
            description=Component.DESCRIPTION,
            input=UpdateTicketInput(),
            output=UpdateTicketOutput(),
        )

    def run(self, params={}):
        client = self.connection.client
        ticket_id = params.get(Input.TICKET_ID)

        # Fetch the current ticket to preserve required fields during update
        current = client.get_ticket(ticket_id)
        payload = dict(current)

        if params.get(Input.TITLE):
            payload["Title"] = params.get(Input.TITLE)
        if params.get(Input.DESCRIPTION):
            payload["Description"] = params.get(Input.DESCRIPTION)
        if params.get(Input.STATUS_ID):
            payload["StatusID"] = params.get(Input.STATUS_ID)
        if params.get(Input.PRIORITY_ID):
            payload["PriorityID"] = params.get(Input.PRIORITY_ID)

        payload.update(params.get(Input.ADDITIONAL_FIELDS, {}))

        client.update_ticket(ticket_id, payload)

        return {Output.SUCCESS: True}

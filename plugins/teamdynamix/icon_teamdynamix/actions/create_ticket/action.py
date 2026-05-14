"""Create Ticket action for TeamDynamix InsightConnect plugin."""

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import CreateTicketInput, CreateTicketOutput, Input, Output, Component


class CreateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket",
            description=Component.DESCRIPTION,
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    def run(self, params={}):
        client = self.connection.client

        payload = {
            "TypeID": params.get(Input.TYPE_ID),
            "Title": params.get(Input.TITLE),
            "AccountID": params.get(Input.ACCOUNT_ID),
            "StatusID": params.get(Input.STATUS_ID),
            "PriorityID": params.get(Input.PRIORITY_ID),
            "RequestorEmail": params.get(Input.REQUESTOR_EMAIL),
            "Description": params.get(Input.DESCRIPTION, ""),
        }

        # Optional fields — only include if provided
        if params.get(Input.FORM_ID):
            payload["FormID"] = params.get(Input.FORM_ID)
        if params.get(Input.RESPONSIBLE_GROUP_ID):
            payload["ResponsibleGroupID"] = params.get(Input.RESPONSIBLE_GROUP_ID)

        # Merge any additional custom fields
        payload.update(params.get(Input.ADDITIONAL_FIELDS, {}))

        response = client.create_ticket(payload)

        ticket_id = response.get("ID")
        if not ticket_id:
            raise PluginException(
                cause="TeamDynamix did not return a ticket ID.",
                assistance="Verify all required fields are valid in your TeamDynamix instance.",
                data=str(response),
            )

        ticket_url = f"{client.base_url}/TDClient/{client.app_id}/Requests/TicketDet?TicketID={ticket_id}"

        return {
            Output.TICKET_ID: ticket_id,
            Output.TICKET_URL: ticket_url,
            Output.SUCCESS: True,
        }

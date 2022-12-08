import insightconnect_plugin_runtime
from .schema import UpdateTicketInput, UpdateTicketOutput, Input, Output, Component

# Custom imports below
from icon_freshservice.util.helpers import clean_dict
from icon_freshservice.util.helpers import dict_keys_to_camel_case


class UpdateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ticket",
            description=Component.DESCRIPTION,
            input=UpdateTicketInput(),
            output=UpdateTicketOutput(),
        )

    def run(self, params={}):
        ticket_id = params.get(Input.TICKETID)
        attachments = params.get(Input.ATTACHMENTS)
        json_data = {
            "name": params.get(Input.NAME),
            "requester_id": params.get(Input.REQUESTERID),
            "email": params.get(Input.EMAIL),
            "phone": params.get(Input.PHONE),
            "subject": params.get(Input.SUBJECT),
            "description": params.get(Input.DESCRIPTION),
            "status": params.get(Input.STATUS),
            "priority": params.get(Input.PRIORITY),
            "impact": params.get(Input.IMPACT),
            "urgency": params.get(Input.URGENCY),
            "type": params.get(Input.TYPE),
            "responder_id": params.get(Input.RESPONDERID),
            "due_by": params.get(Input.DUEBY),
            "fr_due_by": params.get(Input.FRDUEBY),
            "source": params.get(Input.SOURCE),
            "custom_fields": params.get(Input.CUSTOMFIELDS),
            "tags": params.get(Input.TAGS),
            "group_id": params.get(Input.GROUPID),
            "department_id": params.get(Input.DEPARTMENTID),
            "category": params.get(Input.CATEGORY),
            "sub_category": params.get(Input.SUBCATEGORY),
            "item_category": params.get(Input.ITEMCATEGORY),
            "assets": params.get(Input.ASSETS),
        }
        response = self.connection.api.update_ticket(ticket_id, clean_dict(json_data))
        if attachments:
            response = self.connection.api.update_ticket(ticket_id, attachments=attachments)
        return {Output.TICKET: dict_keys_to_camel_case(response.get("ticket", {}))}

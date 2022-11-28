import insightconnect_plugin_runtime
from .schema import CreateTicketInput, CreateTicketOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_freshservice.util.helpers import clean_dict
from icon_freshservice.util.helpers import dict_keys_to_camel_case


class CreateTicket(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ticket",
            description=Component.DESCRIPTION,
            input=CreateTicketInput(),
            output=CreateTicketOutput(),
        )

    def run(self, params={}):
        requester_id = params.get(Input.REQUESTERID)
        email = params.get(Input.EMAIL)
        phone = params.get(Input.PHONE)
        attachments = params.get(Input.ATTACHMENTS)
        if not phone and not requester_id and not email:
            raise PluginException(
                cause="The requester has not been provided.",
                assistance="Please provide phone, ID or email of the requester.",
            )
        json_data = {
            "name": params.get(Input.NAME),
            "requester_id": requester_id if requester_id else None,
            "email": email if email else None,
            "phone": phone if phone else None,
            "subject": params.get(Input.SUBJECT),
            "description": params.get(Input.DESCRIPTION),
            "status": params.get(Input.STATUS),
            "priority": params.get(Input.PRIORITY),
            "impact": params.get(Input.IMPACT),
            "urgency": params.get(Input.URGENCY),
            "type": params.get(Input.TYPE),
            "responder_id": params.get(Input.RESPONDERID),
            "cc_emails": params.get(Input.CCEMAILS),
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
        response = self.connection.api.create_ticket(clean_dict(json_data)).get("ticket", {})
        if attachments:
            response = self.connection.api.update_ticket(response.get("id"), attachments=attachments).get("ticket", {})
        return {Output.TICKET: dict_keys_to_camel_case(response)}
